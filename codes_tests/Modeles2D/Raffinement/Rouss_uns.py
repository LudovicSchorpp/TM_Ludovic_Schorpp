# functions adapted to unstructured grid
import flopy as fp
import numpy as np
import pandas as pd

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