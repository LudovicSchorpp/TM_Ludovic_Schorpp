# this module groups some functions that can be used to extract the budget data from the cbc file of flopy

import flopy as fp
import numpy as np
import pandas as pd

def flows_Z2Z(z1,z2,zones=zones,ia=ia,ja=ja,flowja=flowja,return_map=False):
    
    """
    Total flows from one zone to another
    
    """
    arr = np.zeros([nlay*nrow*ncol])
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
                arr[celln] = flowja[ipos]
                
    if return_map:
        return flow_pos,flow_neg,arr
    else:
        return flow_pos,flow_neg
    
    
def flows_Pack2Z(pack,z1,zones=zones):
    
    """
    
    Calculate the flux from/to a modflow pack to/from a certain zone
    pack : the package budget data from the cbc file for example : cbc.get_data(text="chd")[0]
    z1 : the number of the zone that we want to investigate
    zones : the numpy 2D/3D array containing infos about zones
    return : IN/OUT flux (from/to) 
    
    """
    
flow_pos=0
flow_neg=0
for q1 in pack:
    if zones[q1[0]]==z1:

        if q1[2]>0:
            flow_pos += q1[2]
        else:
            flow_neg -= q1[2]

return flow_pos,flow_neg


