# useful hand-mades functions to import,pre-process data in 3D

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
        result = result[result.areas>(np.max(result.areas)/3)] # only take into account cells that have a least 1/3 area intersected by the polygon
        
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
def importWells3D(path,grid,lst_domain,fac=1/365/86400,V_col="V Bancaris",geol_col="NAPPE_CAPT",
                  geol_layer=["PLIOCENE","QUATERNAIRE"],layer_num=[1,0]):
    
    """
    extract the infos about the amount of water uptake by wells
    path : path to the shp (multi points required)
    grid : the modelgrid
    fac : the factor to transform volume units to get m3/s (depends of original units)
    V_col : the column name containing info about Volume
    geol_col = the column name containing geol infos
    geol_layer : the name of the differents lithology encountered 
    layer_num : the num layer corresponding to the lithology in geol_layer
    """
    
    ix=GridIntersect(grid)
    BD_prlvm = gp.read_file(path)
    stress_data_well=[]
    
    for ilayer in range(len(geol_layer)): # iterate through layers
        BD = BD_prlvm[BD_prlvm[geol_col] == geol_layer[ilayer]] # only keep layers with the right geol
        for o in BD.index: #iterate through each well
            Vw = BD.loc[o,V_col]
            if not (np.isnan(Vw)) | (Vw == 0): #keep productive well
                    cellidx = ix.intersect_point(BD.geometry[o]).cellids[0][0]
                    cellidy = ix.intersect_point(BD.geometry[o]).cellids[0][1]
                    cellid = (layer_num[ilayer],cellidx,cellidy) #cell on which the well is active
                    if cellid in lst_domain: # check if the well is in the domain
                        stress_data_well.append((cellid,-fac*Vw))
    
    return stress_data_well