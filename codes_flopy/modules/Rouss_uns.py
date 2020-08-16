# functions adapted to unstructured grid
import flopy as fp
import numpy as np
import pandas as pd
import geopandas as gp
import sys
from flopy.utils.gridgen import Gridgen 
from flopy.utils.gridintersect import GridIntersect
from flopy.utils import Raster
import shapely
from shapely.geometry import Polygon, Point, LineString, MultiLineString, MultiPoint, MultiPolygon,shape
from shapely.strtree import STRtree  

# hand made functions
from Rouss import *

#1bis
def gridgen2grid(g):
    
    """
    Extract properties from a gridgen object in a disv format
    """
    
    gridprops = g.get_gridprops_disv()
    ncpl = gridprops['ncpl']
    nvert = gridprops['nvert']
    vertices = gridprops['vertices']
    cell2d = gridprops['cell2d']
    
    grid = fp.discretization.VertexGrid(vertices,cell2d,ncpl=ncpl)
    return grid

#2
def gp2lst(gp,featurestype = "polygon"):
    
    """
    Convert a geopandas polygon in a list of coordinates in order to use them in gridgen
    """
    if featurestype == "polygon":
        coord = []
        for x,y in zip (gp.geometry[0].boundary.xy[0],gp.geometry[0].boundary.xy[1]):
            coord.append((x,y))
        return [[coord]] 
    
    if featurestype == "line":
        coord = []
        for x,y in zip (gp.geometry[0].xy[0],gp.geometry[0].xy[1]):
            coord.append((x,y))
        return [[coord]] 
    
    else:
        raise "Enter a valid geometry (polygon or line)"
        
        
#3
def get_cellcenters_disv (grid,cellids): 
    """
    This function return the x and y coordinates of a given cellid and a grid (disv only)
    """
    xc=[];yc=[]
    
    for i in cellids:
        xc.append(grid.xcellcenters[i])
        yc.append(grid.ycellcenters[i])
    return xc,yc

#4
def add_river_disv(riv_path,stations_csv,g,us,ds,lst_chd,lst_domain,grid,cell2dF,layer):
    
    """
    Add a river to a gwf model with a disv discretization
    
    riv_path : The path to the shp of the river (linestring)
    stations_csv : a csv file containing some x,y,z from the river
    g : a gridgen object
    us,ds : up and downstream elevation
    lst_chd : the current list of all the constant heads of the model
    grid : the disv grid (fp.discretization.VertexGrid)
    cell2DF : a dataframe containing cell2d infos (pd.DataFrame(g.get_gridprops_disv()["cell2d"]))
    layer : int, on which layer is the river ?
    
    """
    Riv_gp = gp.read_file(riv_path) # import the shp with gp
    coord_riv=[]                     # ini the list that will contains the coordinates
    for x,y in zip(Riv_gp.geometry[0].xy[0],Riv_gp.geometry[0].xy[1]): # a loop to extract coordinates with zip
        coord_riv.append((x,y))
    
    df_riv=pd.DataFrame()
    inter = g.intersect([[coord_riv]],"line",0) # do the intersection
    df_riv = pd.DataFrame({"cellids":inter.nodenumber,"lengths":inter.length},dtype=int)  #store it in a df 
    df_riv = df_riv.groupby(["cellids"],sort=False).sum() # groupby multiple cells and sum the lengths 
    df_riv.reset_index(inplace=True)
    
    df_riv["head"] = np.zeros([df_riv.shape[0]])
    df_riv.loc[0,"head"] = us
    df_riv.loc[df_riv.index[-1],"head"] = ds
    
    riv_stations = pd.read_csv(stations_csv,sep=";")

    ### block to attribute xc and yc at each cell (xcenter and ycenter), the normal way to do it is grid.xcellcenter(cellid) 
    #   but it's pretty slow. Here i'm using a df containing infos about each cell (cell2dF)
    for cellid in df_riv.cellids:
        if (cellid < 0): # drop cells outside of the domain
            df_riv = df_riv.drop(df_riv[df_riv["cellids"] == cellid].index)
    df_riv.reset_index(inplace = True)
    
    for i in range(df_riv.shape[0]):
        df_riv.loc[i,"xc"],df_riv.loc[i,"yc"] = cell2dF[cell2dF.iloc[:,0] == df_riv.loc[i,"cellids"]].iloc[0,1:3]
    ###-------------------------------------------------------------------------------------------------------------

    
    ### block stations----------------------------------------------------------------------------------------------
    for i in riv_stations.index:
        xs = riv_stations.loc[i].x
        ys = riv_stations.loc[i].y
        elev = riv_stations.loc[i].elev
        dist = ((df_riv["xc"] - xs)**2 + (df_riv["yc"] - ys)**2)**0.5
        df_riv.loc[dist==np.min(dist),"head"] = elev - 1
    ###-------------------------------------------------------------------------------------------------------------
    
    
    ### interpolation btw points------------------------------------------------------------------------------------
    linInt_Dfcol(df_riv,col="head")
    ###-------------------------------------------------------------------------------------------------------------
    
    
    ### droppping cells---------------------------------------------------------------------------------------------
    for cellid in df_riv.cellids:
            if (cellid in lst_chd) | (cellid not in lst_domain):
                df_riv = df_riv.drop(df_riv[df_riv["cellids"] == cellid].index)
    ###-------------------------------------------------------------------------------------------------------------
    
    
    ### create the stress package-----------------------------------------------------------------------------------
    df_riv.reset_index(inplace=True)
    H_riv = df_riv["head"]
    riv_chd=[]; o =-1;
    for x in df_riv.cellids:
        o = o + 1
        riv_chd.append(((layer,x),H_riv[o]))
        lst_chd.append(x)
    return riv_chd
    ###-------------------------------------------------------------------------------------------------------------
  


 #5
def import_rch_disv(file,grid,coeff=0.5):
    
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
    rcha = rch_areas.resample_to_grid(np.array(grid.xcellcenters),
                                      np.array(grid.ycellcenters),
                                      band = rch_areas.bands[0],
                                    method="nearest")

    rcha[rcha==0]=np.mean(rcha[rcha!=0])
    coeff = 0.5 # part de pluie qui s'infiltre
    rcha *= coeff
    return rcha