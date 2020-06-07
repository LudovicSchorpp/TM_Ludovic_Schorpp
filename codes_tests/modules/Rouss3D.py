# useful hand-mades functions to import and pre-process data in 3D

import flopy as fp
import numpy as np
import geopandas as gp
import pandas as pd
import os
import gdal
import matplotlib.pyplot as plt
from flopy.utils.gridgen import Gridgen 
from flopy.utils.gridintersect import GridIntersect
import shapely
from shapely.geometry import Polygon, Point, LineString, MultiLineString, MultiPoint, MultiPolygon
from shapely.strtree import STRtree  


#1
def gp2cellids3D (grid, gp, idomain, idomain_active=True, type = "polygon",layer=0,areas=3):
    """
    this function extract the cellids of the intersection between a geopandas object and a grid 
    grid : modelgrid
    gp : geopandas object (polygon, linestring only)
    idomain : the idomain array to update it (3d list)
    idomain_active : bool, if true the idomain is update (cells intersect by the gp will be noted as active), prevents some issues
    type : str, features type (polygon or line)
    layer : int, the layer on which is the gp
    areas : factor that determine if a cell is accounted intersected or not based on the total area intersected in this cell 
    (a value of 3, for example, mean only cells which have 1/3 of their area intersected by the polygon will be taken into account)
    """
    
    
    ix = GridIntersect(grid)
    if type == "polygon":
        result = ix.intersect_polygon(gp.geometry[0])
        result = result[result.areas>(np.nanmax(result.areas)/3)] # only take into account cells that have a least 1/3 area intersected 
        result = result[result.areas!=0]                       # fix bug
    
    if type == "boundary" :
        result = ix.intersect_linestring(gp.geometry[0].boundary)

    if type == "line" :
        result = ix.intersect_linestring(gp.geometry[0])
        
    lst=[];
    for irow, icol in result.cellids:
        lst.append(((layer,irow,icol)))
        if idomain_active:
            idomain[layer,irow,icol] = 1
    return lst


#2
def importWells3D(BD_prlvm,grid,lst_domain,fac=1/365/86400,V_col="V Bancaris",geol_col="NAPPE_CAPT",
                  geol_layer=["PLIOCENE","QUATERNAIRE"],layer_num=[1,0]):
    
    """
    extract the infos about the amount of water uptake by wells
    BD_prlvm : geopanda object (multiple point). Must have a volume col, geology col,
    grid : the modelgrid
    fac : the factor to transform volume units to get m3/s (depends of original units)
    V_col : the column name containing info about Volume
    geol_col = the column name containing geol infos
    geol_layer : the name of the differents lithology encountered 
    layer_num : the num layer corresponding to the lithology in geol_layer
    note : multiple layer can be assigned to one lithology (assign multiple number in layer_num),
    in that case the flux will be equally separate through each specified layer
    """
    
    ix=GridIntersect(grid)
    stress_data_well=[]
    
    for ilayer in range(len(geol_layer)): # iterate through layers
        BD = BD_prlvm[BD_prlvm[geol_col] == geol_layer[ilayer]] # only keep layers with the right geol
        for o in BD.index: #iterate through each well
            Vw = BD.loc[o,V_col]
            if not (np.isnan(Vw)) | (Vw == 0): #keep productive well
                    cellidx = ix.intersect_point(BD.geometry[o]).cellids[0][0]
                    cellidy = ix.intersect_point(BD.geometry[o]).cellids[0][1]
                    
                    if type(layer_num[ilayer]) == int :
                        cellid = (layer_num[ilayer],cellidx,cellidy) #cell on which the well is active
                        if cellid in lst_domain: # check if the well is in the domain
                            stress_data_well.append((cellid,-fac*Vw))
                    elif len(layer_num[ilayer]) > 1:
                        cpt=0
                        for isublay in layer_num[ilayer]:
                            cellid = (isublay,cellidx,cellidy)

                            if cellid in lst_domain:
                                cpt+=1
                        for isublay in layer_num[ilayer]:   
                            cellid = (isublay,cellidx,cellidy)
                            if cellid in lst_domain: # check if the well is in the domain
                                stress_data_well.append((cellid,-fac*Vw/cpt))
    
    return stress_data_well



#4
def up_act_cell(idomain):
    
    """
    return the uppermosts active cells from a 3D list idomain (1: active)
    idomain : shape (nlay,nrow,ncol)
    """
    
    lst_dom_act=[]
    nlay = idomain.shape[0]
    nrow = idomain.shape[1]
    ncol = idomain.shape[2]

    for irow in range(nrow):
        for icol in range(ncol):
            for ilay in range(nlay):
                idx = (ilay,irow,icol)
                if idomain[idx] == 1:
                    lst_dom_act.append((ilay,irow,icol))
                    break
    return lst_dom_act


    
#6
def assign_k_zones(zone1,k1,k,g,layer):
    
    """
    Assign a certain k in a certain zone for a given layer
    zone1 : the zone format [[[(x,y),(x1,y1),(...),...]]]
    k1 : the permeability of the zone
    layer : int
    k : the 3d list containing the permeability fo the model
    g : gridgen object
    """
    
    res = g.intersect(zone1,"polygon",layer)
    k[res.nodenumber] = k1
    
#7
def shp2idomain(shp_path,g,idomain,features_type="polygon",layer=0):
    
    """
    Turns cells active inside a certain shp, need a gridgen object
    """
    
    if len(idomain.shape) != 1:
        idomain = idomain.reshape(g.nlay*g.nrow*g.ncol) # reshape idomain if not in the right format
    res = g.intersect(shp_path,features_type,layer)
    idomain[res.nodenumber] = 1
    idomain = idomain.reshape(g.nlay,g.nrow,g.ncol)
    
    
#8
def ImportControlPz3D(piez_path,sheet_name,geol_layer,layer_num,geol_col,grid,nlay,np_col="NP",x_col="x",y_col="y"):
    
    """
    return an 3D array containing infos about piezometer level in control pz in a multiple layers model$
    the null value is set to 0
    
    piez_path : str, the file path to the excel sheet
    sheet_name : str, the name of the data sheet 
    geol_layer : lst, the name of the different lithology
    layer_num : lst, the ilay number which corresponds to the lithology in geol_layer
    geol_col : the name of the colum containing lithologies
    grid and nlay : grid and number of layers of the model
    np_col : str, the name of the column containing infos about the PL
    x_col,y_col : str, the name of the columns containings geo infos
    """
    
    piez_path="../../data/piezos/pz_hydriad.xlsx"
    data = pd.read_excel(piez_path,sheet_name=sheet_name)

    geol_layer = geol_layer
    layer_num = layer_num

    Control_pz = np.zeros([nlay,grid.nrow,grid.ncol]) #ini list

    for ilay in range(len(geol_layer)): # go through each different lithology
        lstIDpz=[]
        Pz=[]
        DB = data[data[geol_col]==geol_layer[ilay]]
        DB.reset_index(inplace=True)
        for o in np.arange(DB.shape[0]): # loop to iterate through the data and returns the intersected cellids
            xc = DB[x_col][o]
            yc = DB[y_col][o] 
            cellid = grid.intersect(xc,yc)

            if not np.isnan(DB[np_col][o]):
                lstIDpz.append(cellid)
                Pz.append(DB[np_col][o])

        df = pd.DataFrame()
        df["cellid"]=lstIDpz
        df["Pz"] = Pz
        df = df.groupby(["cellid"]).mean().reset_index() # group pz on the same cell

        for i in df.index:
            j,k = df.loc[i,"cellid"]
            Control_pz[layer_num[ilay],j,k] = df.loc[i,"Pz"]

    return Control_pz