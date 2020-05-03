# this module regroups some functions that can be used to extract the budget data from the cbc file of flopy

import flopy as fp
import numpy as np
import pandas as pd

def flows_Z2Z(z1,z2,zones,ia,ja,cbc,kstpkper=None,return_map=False):
    
    """
    Total flows from one zone to another
    
    """
    nlay = zones.shape[0]
    nrow = zones.shape[1]
    ncol = zones.shape[2]
    zones = zones.reshape(nlay*nrow*ncol)
    arr = np.zeros([nlay*nrow*ncol])
    flowja = cbc.get_data(text='FLOW-JA-FACE',kstpkper=kstpkper)[0][0, 0, :]
    flow_pos=0
    flow_neg=0
    
    for celln in range(ia.shape[0]-1):
        if zones[celln] == z1:
            for ipos in range(ia[celln]+1, ia[celln+1]): # loop for each connexions of celln
                cellm = ja[ipos]  # retrieve cell number of adjacent cell
                if (zones[cellm] == z2):
                    if flowja[ipos]> 0:
                        flow_pos += flowja[ipos]
                    else:
                        flow_neg -= flowja[ipos]
                if return_map:
                    arr[celln] = flowja[ipos]
                
    if return_map:
        return flow_pos,flow_neg,arr
    else:
        return flow_pos,flow_neg
    
    
def flows_Pack2Z(pack,z1,zones):
    
    """
    
    Calculate the flux from/to a modflow pack to/from a certain zone
    pack : the package budget data from the cbc file for example : cbc.get_data(text="chd")[0]
    z1 : the number of the zone that we want to investigate
    zones : the numpy 2D/3D array containing infos about zones (can't be 1D)
    return : IN/OUT flux (from/to) 
    
    """
    nlay = zones.shape[0]
    nrow = zones.shape[1]
    ncol = zones.shape[2]
    zones = zones.reshape(nlay*nrow*ncol)
    flow_pos=0
    flow_neg=0
    for q1 in pack:
        if zones[q1[0]-1]==z1: # nodenumber is one based !

            if q1[2]>0:
                flow_pos += q1[2]
            else:
                flow_neg -= q1[2]
    
    return flow_pos,flow_neg


