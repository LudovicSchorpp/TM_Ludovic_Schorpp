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
def gp2idomain (gp,grid,idomain,area=0,layer=0):
    
    '''
    This function attribute active values to cells given a certain geopandas object and a grid (flopy.discretization) with idomain
    the tolerance is a value that determine at which level a cell will be counted as intersected by the polygon 
    (3 for example mean that only cells that have 1/3 of their area intersected by the polygon will be accounted)
    '''
    
    ix = GridIntersect(grid)
    
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
def gp2cellids (grid, gp, idomain, idomain_active=True, type = "polygon",layer=0):
    """
    this function extract the cellids of the intersection between a geopandas object and a grid 
    """
    
    ix = GridIntersect(grid)
    if type == "polygon":
        result = ix.intersect_polygon(gp.geometry[0])
        #result = result[result.areas>(np.max(result.areas)/3)] # only take into account cells that have a least 1/3 intersected by the polygon
        
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


#5
def get_heads(model_name,workspace):
    """
    Function that return the heads from the headfile
    """
    headfile = '{}.hds'.format(model_name)
    fname = os.path.join(workspace,headfile)    
    hdobj = fp.utils.HeadFile(fname, precision='double')  
    head  = hdobj.get_data()
    return head


def get_spdis(model_name,workspace):
    """
    Function that return the specific discharge from the cbcfile
    """
    spdfile = '{}.cbc'.format(model_name)
    fname = os.path.join(workspace,spdfile)    
    spdobj = fp.utils.CellBudgetFile(fname, precision='double')  
    spd  = spdobj.get_data(text="SPDIS")
    return spd



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
