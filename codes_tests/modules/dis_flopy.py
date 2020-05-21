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
    return a idomain for active zones, base on a numpy 3d array with surfaces
    surf : an array with surfaces, no data == 9999
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
    botm[0][mask] = top[mask] - min_ep_inact
    
    
    #active cells 
    for ilay in range(botm.shape[0]-1):
        mask = ((botm[ilay] - botm[ilay+1])<= min_ep_act) & (idomain[ilay+1]==1)
        botm[ilay+1][mask] = botm[ilay][mask] - min_ep_act
    
    #inactive cells
    for ilay in range(botm.shape[0]-1):
        mask = ((botm[ilay] - botm[ilay+1])<= min_ep_inact) & (idomain[ilay+1]!=1)
        botm[ilay+1][mask] = botm[ilay][mask] - min_ep_inact
        
        
def multi_lay(botm,idomain,ep=50,nsublay=4,layer=2):
    
    """
    subdivised a layer into sublayers, return two numpy 3D array, one is surface and the other the idomain associated 
    to these new layers
    """
    nlay = botm.shape[0]
    nrow = botm.shape[1]
    ncol = botm.shape[2]
    idomain_sub_lay = np.zeros([nsublay,nrow,ncol])
    botm_sub_lay = np.zeros([nsublay,nrow,ncol])
    thk = botm[layer-1]-botm[layer]
    
    #first sublayer
    botm_sub_lay[0] = botm[layer-1]
    botm_sub_lay[0][thk<0.2] -= 0.1
    botm_sub_lay[0][(thk<ep)&(thk>0.2)] = botm[layer][(thk<ep)&(thk>0.2)]
    botm_sub_lay[0][thk>ep] -= ep
    
    #idomain 1st sublayer
    idomain_sub_lay[0][thk>0.2] = 1
    
    #between 1st and nth 
    for isublay in range(1,nsublay-1):
        botm_sub_lay[isublay] = botm_sub_lay[isublay-1].copy()
        botm_sub_lay[isublay][thk<isublay*ep] -= 0.1
        mask = (thk<(ep*(isublay+1)))&(thk>isublay*ep)
        botm_sub_lay[isublay][mask] = botm[layer][mask]
        botm_sub_lay[isublay][thk>(ep*(isublay+1))] -= ep
        
        idomain_sub_lay[isublay][thk>isublay*ep] = 1
    
    if nsublay==2:
        isublay=0
        
    #last sublayer
    botm_sub_lay[-1] =  botm_sub_lay[isublay].copy()
    botm_sub_lay[-1][thk<(isublay+1)*ep] -= 0.1
    mask = (thk>(isublay+1)*ep)
    botm_sub_lay[-1][mask] = botm[layer][mask]

    idomain_sub_lay[-1][thk>(isublay+1)*ep] = 1

    #new subdivised botom
    new_botm = np.ones([nlay+nsublay-1,nrow,ncol])
    new_botm[0:layer]=botm[0:layer]
    new_botm[layer:layer+nsublay] = botm_sub_lay
    new_botm[layer+nsublay:] = botm[layer+1:]
    
    #new subdivised idomain
    new_idomain = np.ones([nlay+nsublay-1,nrow,ncol])
    new_idomain[0:layer]=idomain[0:layer]
    new_idomain[layer:layer+nsublay] = idomain_sub_lay
    new_idomain[layer+nsublay:] = idomain[layer+1:]
    
    return new_botm,new_idomain