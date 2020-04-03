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