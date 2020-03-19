# Very Specific functions that lighten the code, only for the 2d model usage 

import flopy as fp
import numpy as np
import geopandas as gp
import pandas as pd
import os
from osgeo import ogr
import gdal
import matplotlib.pyplot as plt
from flopy.utils.gridgen import Gridgen 
from flopy.utils.gridintersect import GridIntersect
from flopy.utils import Raster
import shapely
from shapely.geometry import Polygon, Point, LineString, MultiLineString, MultiPoint, MultiPolygon,shape
from shapely.strtree import STRtree  

from Rouss1 import *

def import_rch(file,grid,coeff=0.5):
    
    """
    Return an array of the recharge from a given raster file (efficient rain) and a runoff coefficient (can be a 2D)
    Raster from flopy must be imported
    rcha = import_rch(file,coef)
    file : the path to the raster
    coeff : the runoff coefficient
    grid : the modelgrid from flopy.discretization
    """
    rcha=[]
    rch_areas = Raster.load(file)
    rcha = rch_areas.resample_to_grid(grid.xcellcenters,
                            grid.ycellcenters,
                            band = rch_areas.bands[0],
                            method="nearest")

    rcha[rcha==0]=np.mean(rcha[rcha!=0])
    coeff = 0.5 # part de pluie qui s'infiltre
    rcha *= coeff
    return rcha

def Complete_riv(riv_path,stations_csv,us,ds,lst_chd,lst_domain,grid):
    
    """
    a complete function that import a river into the modflow 6 and return the stress data.
    the river path, the station path and the upstream and downstream head must be provided
    
    riv_path : the path to the shapefile of the river (one linestring only)
    stations_csv : path to the csv file containing the infos about the stations (x,y,elevation)
    lst_chd : a list of every cells constant heads
    lst_domain : a list of each active cell
    grid : grid of the model
    """
    
    BC_riv = gp.read_file(riv_path) # read shp, linestring from ups to dws
    df_riv = import_riv(grid,BC_riv) # extract cellids intersected + lengths in each cells
    df_riv["xc"],df_riv["yc"] = get_cellcenters(grid,df_riv.cellids)
    df_riv["head"] = np.zeros([df_riv.shape[0]])

    # us and ds heads
    df_riv["head"].iloc[0] = us
    df_riv["head"].iloc[-1] = ds
    
    # station(s) and assignement of heads/
    riv_stations = pd.read_csv(stations_csv,sep=";")
    for i in riv_stations.index:
        xs = riv_stations.loc[i].x
        ys = riv_stations.loc[i].y
        elev = riv_stations.loc[i].elev
        dist = ((df_riv["xc"] - xs)**2 + (df_riv["yc"] - ys)**2)**0.5
        df_riv.loc[dist==np.min(dist),"head"] = elev

    # interpolation of the heads btw ups,stations and ds
    linInt_Dfcol(df_riv,col="head")

    
    # drop some cells
    for cellid in df_riv.cellids:
        if (cellid in lst_chd):
            df_riv = df_riv.drop(df_riv[df_riv["cellids"] == cellid].index)
        if cellid not in lst_domain:
            df_riv = df_riv.drop(df_riv[df_riv["cellids"]== cellid].index)
    
    # create the stress package
    df_riv= df_riv.reset_index()
    H_riv = df_riv["head"]
    riv_chd=[]; o =-1;
    for x in df_riv.cellids:
        o = o + 1
        riv_chd.append((x,H_riv[o]))
        lst_chd.append(x)
    return riv_chd

    
