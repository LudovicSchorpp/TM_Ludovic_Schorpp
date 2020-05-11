import flopy as fp
import numpy as np
import geopandas as gp
import pandas as pd


def check_thk(top,botm):
    """
    check if a cell have a thickness <= 0 for each layer
    input : top (the top surface) and botm (botom of each layer)
    output : lst of bool (false mean everything's okay)
    """
    nlay = botm.shape[0]
    bol_lst=[]
    bol_lst.append(((top-botm[0])<=0).any())
    for ilay in range(nlay-1):
        bol_lst.append(((botm[ilay]-botm[ilay+1])<=0).any())
    return bol_lst

#3
def active_dom(surf,grid,nodata=9999):
    
    """
    return a idomain for active zones, base on surfaces
    surf : an array with no data zones == 9999
    grid : modelgrid
    """
    idomainQ = np.zeros([grid.nrow,grid.ncol])
    idomainQ[surf != nodata] = 1
    return idomainQ

#5
def MinThick(idomain,botm,top,min_ep_act=5,min_ep_inact=0.1):
    
    """
    Change the thickness of certains cells based on a criterion (min_ep_act for active cells and min_ep_inact for inactive cells)
    Can also be used to change cells with negative thickness
    
    idomain : 3d list (nlay,nrow,ncol)
    botm : the list containing every surfaces of all the layers
    top : the top surface
    min_ep : int, the minimum thickness tolerate
    """
    
    #active cells (1st layer)
    mask = ((top-botm[0])<= min_ep_act) & (idomain[0]==1)
    botm[0][mask] = top[mask] - min_ep_act
    
    #inactive cells (1st layer)
    mask = ((top-botm[0])<= min_ep_inact) & (idomain[0]!=1)
    top[mask] = botm[0][mask] + min_ep_inact
    
    
    #active cells 
    for ilay in range(botm.shape[0]-1):
        mask = ((botm[ilay] - botm[ilay+1])<= min_ep_act) & (idomain[ilay+1]==1)
        botm[ilay+1][mask] = botm[ilay][mask] - min_ep_act
    
    #inactive cells
    for ilay in range(botm.shape[0]-1):
        mask = ((botm[ilay] - botm[ilay+1])<= min_ep_inact) & (idomain[ilay+1]!=1)
        botm[ilay+1][mask] = botm[ilay][mask] - min_ep_inact
        
        
