# some useful "hand-made" functions

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
def Imreduction (imar, nrow, ncol):
    
    """
    This function reduce the dimensionality of an image.
    An array of the image must be provided by the user, same for the number of row and col of the new image
    No data should be specified as "None" type
    return a new array
    """
    
    #first define the ratio between the given and the desired resolution in x and y
    facR=imar.shape[0]/nrow
    facC=imar.shape[1]/ncol
    
    # go through the entire grid (nrow,ncol) and use the mean of all the values in the array image
    # in a specific cell of the grid (i,o)
    new_imar=[]
    for i in range(nrow):
        for o in range(ncol):
            new_val=np.nanmean(imar[np.round(i*facR).astype(int):np.round(i*facR+facR).astype(int),
                                    np.round(o*facC).astype(int):np.round(o*facC+facC).astype(int)])
            new_imar.append(new_val)
    
    # create an array of the new image array
    new_imar = np.array(new_imar)
    return np.array(pd.DataFrame(new_imar.reshape(nrow,ncol)).fillna(0))


#2
def gp2idomain (gp,grid,idomain,area=0,layer=0,method="none"):
    
    '''
    This function attribute active values to cells given a certain geopandas object and a grid (flopy.discretization) with idomain
    the area is a value that determine at which level a cell will be counted as intersected by the polygon 
    (3 for example mean that only cells that have 1/3 of their area intersected by the polygon will be accounted)
    '''
    if method == "none":
        ix = GridIntersect(grid)
    if method == "structured":
        ix = GridIntersect(grid,method=method)
    
    if area == 0:
        result = ix.intersect_polygon(gp.geometry[0])
    
    if area >= 1:
        result = ix.intersect_polygon(gp.geometry[0])
        result = result[result.areas>(np.max(result.areas)/area)]
        
    lst=[]
    for irow, icol in result.cellids:
        idomain[irow*grid.ncol+icol]=1
        lst.append(((layer,irow,icol)))
    return lst



#3
def gp2cellids (grid, gp, idomain, idomain_active=True, type = "polygon",layer=0,areas=3):
    """
    this function extract the cellids of the intersection between a geopandas object and a grid 
    """
    
    ix = GridIntersect(grid)
    if type == "polygon":
        result = ix.intersect_polygon(gp.geometry[0])
        result = result[result.areas>(np.max(result.areas)/3)] # only take into account cells that have a least 1/3 intersected by the polygon
        
    if type == "boundary" :
        result = ix.intersect_linestring(gp.geometry[0].boundary)

        
    if type == "line" :
        result = ix.intersect_linestring(gp.geometry[0])
        
    lst=[];
    for irow, icol in result.cellids:
        lst.append(((layer,irow,icol)))
        if idomain_active:
            idomain[irow*grid.ncol+icol] = 1
    return lst



#4
def cellidBD(lst_in, layer=0):   
    """
    extract the cellids at the boundary of the domain at a given layer
    """
    lst_bc=[]
    lst_in2=np.array(lst_in)
    for i in range(len(lst_in)):
        xl=lst_in[i][1]
        yl=lst_in[i][2]
        rec = (xl,yl)
        recx1 = (layer,xl+1,yl)
        recx_1= (layer,xl-1,yl)
        recy1 = (layer,xl,yl+1)
        recy_1= (layer,xl,yl-1)
        voisins = [recx1,recx_1,recy1,recy_1];
        for k in voisins:
            mask = (lst_in2==k)[:,1]*(lst_in2==k)[:,2]
            if lst_in2[mask].size == 0:
                lst_bc.append(rec)
                break # if it finds a neighbour that is not in the list --> stores it and break !
                
    lst_bc2 = np.array(lst_bc)
    lst_bc=[]
    for x,y in lst_bc2:
        a = (layer,x,y) # (layer,row,col)
        lst_bc.append(a)
    return lst_bc


# 5 visualization functions
def get_heads(model_name,workspace):
    """
    Function that returns the heads from the headfile
    """
    headfile = '{}.hds'.format(model_name)
    fname = os.path.join(workspace,headfile)    
    hdobj = fp.utils.HeadFile(fname, precision='double')  
    head  = hdobj.get_data()
    return head


def get_spdis(model_name,workspace):
    """
    Function that returns the specific discharge from the cbcfile
    """
    spdfile = '{}.cbc'.format(model_name)
    fname = os.path.join(workspace,spdfile)    
    spdobj = fp.utils.CellBudgetFile(fname, precision='double')  
    spd  = spdobj.get_data(text="SPDIS")
    return spd

def get_budgetobj(model_name,workspace):
    """
    Function that returns the budget file as an object
    """
    lstBudgetfile = "{}.lst".format(model_name)
    fname = os.path.join(workspace,lstBudgetfile)
    Budgetobj = fp.utils.Mf6ListBudget(fname)
    return Bugetobj


#6
def get_MNTbbox (MNT_path):
    """
    Function that returns the x0,y0,x1 and y1 (in this order) of a mnt in the mnt's Coord. Sys.
    """
    
    R_mnt = gdal.Open(MNT_path)
    mnt_infos=R_mnt.GetGeoTransform()
    x0 = mnt_infos[0]+mnt_infos[1]/2
    x1 = x0 + R_mnt.RasterXSize*mnt_infos[1]
    y1 = mnt_infos[3]+mnt_infos[5]/2
    y0 = y1 + R_mnt.RasterYSize*mnt_infos[5]
    
    return x0,y0,x1,y1


#7
def inter_lst (lst1,lst2,typ = "intersection"):
    """
    return the intersection/unique values of the list1 compared to list2
    """
    
    if typ == "intersection":
        return [i for i in lst1 if i in lst2]
    if typ == "unique":
        return [i for i in lst1 if i not in lst2]
        
#8
def import_riv(grid,gp):
    """
    This function extract infos about a river (geopandas object, LINESTRING),cellids + lengths of in each cells in the right order. 
    Format : import_riv (Grid (from the gwf model, gwf.modelgrid for ex.), gp (a geopandas object containing a unique Linestring))
    Return a dataframe containing these datas, post-processing necessary to remove cells that are already counted as BC in the model
    """
    
    ix = GridIntersect(grid)
    coord_riv=[]
    for x,y in zip(gp.geometry[0].xy[0],gp.geometry[0].xy[1]):
        coord_riv.append((x,y))

    verti=[]
    df_tot_ord = pd.DataFrame() # empty DF
    for i in range(len(coord_riv)):
        if i < len(coord_riv)-1:
            lsi = LineString([coord_riv[i],coord_riv[i+1]]) # create the linestring btw point i and i+1
            res = ix.intersect_linestring(lsi) # do the intersection
            cellids = res.cellids # extract cellids

            if len(cellids)>1: # if more than one cells is intersected --> we need to order them

                dirx = coord_riv[i+1][0]-coord_riv[i][0] # Xdirection of the linestring

                for x,y in res.vertices: # extract the 1st vertice of the intersections in order to organize 
                    verti.append(x)
                vertix = np.array(verti)[:,0]
                df = pd.DataFrame({"cellids":cellids,"vertix":vertix,"lengths":res.lengths}) # create a DF to order
                verti=[]

                #organize the cells given the direction
                if dirx > 0:
                    df.sort_values(by=["vertix"],ascending=True,inplace=True)                
                if dirx < 0:
                    df.sort_values(by=["vertix"],ascending=False,inplace=True) 

                # append these data in a big DF
                df_tot_ord = df_tot_ord.append(df).drop(["vertix"],axis=1)

            else : # if only one cell is intersected by the linestring
                df_tot_ord = df_tot_ord.append(pd.DataFrame({"cellids":cellids,"lengths":res.lengths}))

    df_riv = df_tot_ord.groupby(["cellids"],sort=False).sum()

    # retrieve data
    lst_len_Riv = df_riv["lengths"].values

    cellids_Riv=[]; # list of all the cells intersected by the river
    cellids = df_riv.index
    for irow,icol in cellids:
        cell = (0,irow,icol)
        if cell not in cellids_Riv:
            cellids_Riv.append(cell)

    df_riv = pd.DataFrame({"cellids":cellids_Riv,"lengths":lst_len_Riv})
    
    
    return df_riv
    

#9
def get_cellcenters (gwf,cellids): 
    """
    This function return the x and y coordinates of a given cellid and a gwf model (dis only)
    """
    xc=[];yc=[]
    for i,j,k in cellids:
        xc.append(gwf.modelgrid.xcellcenters[j,k])
        yc.append(gwf.modelgrid.ycellcenters[j,k])

    return xc,yc

#10

def lin_interp(lengths,Hv,Lv):
    """
    function that realize a linear interpolation btw 2 values, given a certain list of weigth (lengths typically for a river)
    """
    
    ar_long = np.array(lengths)
    dh_dl = (Lv-Hv)/lengths.sum()
    H_riv = np.zeros(ar_long.shape[0],dtype=np.float)    
    for idx in range(ar_long.shape[0]):
        if idx == 0:
            len_cum = 0.5 * ar_long[0]
        else:
            len_cum += 0.5 * (ar_long[idx-1]+ar_long[idx])
        H_riv[idx] = Hv + len_cum * dh_dl
    return H_riv

#11
def ibd_bcdata(bc,iper=0,ilay=0):
    """
    Function that return the position of the bc of a given a bc package and for a certain period and layer
    """
    ibd = np.ones((nlay, nrow, ncol), dtype=np.int)
    
    ra = bc.stress_period_data.get_data(iper)   
    for k, i, j in ra['cellid']:
        ibd[k, i, j] = -1
    
    return ibd