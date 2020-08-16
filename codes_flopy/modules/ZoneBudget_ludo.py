# this module regroups some functions that can be used to extract the budget data from the cbc file of flopy

import flopy as fp
import numpy as np
import pandas as pd

#0
def reshapeZones(zones):
    nlay = zones.shape[0]
    nrow = zones.shape[1]
    ncol = zones.shape[2]
    zones_reshape = zones.reshape(nlay*nrow*ncol)
    return zones_reshape


#1
def flows_Z2Z(z1,z2,zones,ia,ja,cbc,kstpkper=None):
    
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
                    
                    arr[ipos]=flowja[ipos]
                
    return flow_pos,flow_neg,arr
    
#2    
def flows_Pack2Z(pack,z1,zones):
    
    """
    Calculate the flux from/to a modflow package to/from a given zone
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
    
    if z1 in np.unique(zones[pack.node-1]):
        for q1 in pack:
            if zones[q1[0]-1]==z1: # nodenumber is one based !

                if q1[2]>0:
                    flow_pos += q1[2]
                else:
                    flow_neg -= q1[2]
    
    return flow_pos,flow_neg

#3
def get_nzones(zones):
    """
    return the number of zones from a zone array (0 is a null value)
    """
    nzones = np.unique(zones).shape[0]
    if 0 in np.unique(zones):
        nzones -=1
    return nzones

def get_dfpos(zones,ia,ja):
    
    """
    Return a df containing infos of connexion between interzones cells, can be reused at different times
    """
    
    def comb(m, lst):
        if m == 0: return [[]]
        return [[x] + suffix for i, x in enumerate(lst)
                for suffix in comb(m - 1, lst[i + 1:])]
    seq=[]
    for zone in np.unique(zones):
        if zone != 0:
            seq.append(int(zone))
    lst_comb = comb(2, seq)
    
    zones = reshapeZones(zones)
    lst_ipos=[]
    fromz2z=[]

    for zz in lst_comb:
        z1=zz[0]
        z2=zz[1]
        for celln in range(ia.shape[0]-1):
            if zones[celln] == z1:
                for ipos in range(ia[celln]+1, ia[celln+1]): # loop for each connexions of celln
                    cellm = ja[ipos]  # retrieve cell number of adjacent cell
                    if (zones[cellm] == z2):
                        lst_ipos.append(ipos)
                        fromz2z.append("{}to{}".format(z1,z2))
    df_pos = pd.DataFrame({"ipos":lst_ipos,"dir":fromz2z})
    return df_pos


def flow_zz(cbc,df_pos,zones,kstpkper=None):
    
    """
    Return a matrix containing flux btw differents zones (each 2 columns correspond to one zone (1st is IN and 2nd OUT from the zone)
    each layer represent a zone (from zone 1 to zone n)
    cbc : cbc object
    df_pos : Dataframe with infos of connexions btw interzones cells (see get_dfpos)
    zones : the numpy 3D array with the zones
    kstpkper : array of size 2, indices that indicates stress period and time step
    """
    
    nzones = get_nzones(zones)
    flowja = cbc.get_data(text='FLOW-JA-FACE',kstpkper=None)[0][0, 0, :]
    FluxZZ = np.zeros([nzones,2*nzones]) # interzones flows matrix
    
    for idir in df_pos.dir.unique():
        flow_pos=0
        flow_neg=0
        df_tmp = df_pos[df_pos.dir==idir]
        for ipos in df_tmp.ipos:
            if flowja[ipos]> 0:
                flow_pos += flowja[ipos]
            else:
                flow_neg -= flowja[ipos]
            
        FluxZZ[int(idir[-1])-1,(int(idir[0])*2-2):(int(idir[0])*2)] = (flow_pos,flow_neg)
        FluxZZ[int(idir[0])-1,(int(idir[-1])*2-2):(int(idir[-1])*2)] = (flow_neg,flow_pos)
    return FluxZZ


def flow_pack(cbc,zones,kstpkper=None,n=1):
    
    """
    Return a df whith flux from/to zones/packages
    """
    
    DF_pack = pd.DataFrame()
    for z in np.unique(zones):
        if z != 0:
            pos=[]
            neg=[]
            pack_list=[]
            for i in range(pd.DataFrame(cbc.recordarray).shape[0]-n):
                pack = cbc.get_data(i+n,kstpkper=None)[0]
                posi,negi = flows_Pack2Z(pack,z,zones=zones)
                pos.append(posi)
                neg.append(negi)
            z_DF = pd.concat([pd.DataFrame(pos),pd.DataFrame(neg)],axis=1)
            DF_pack = pd.concat([DF_pack,z_DF],axis=1)
            
    return DF_pack


def index_pack(cbc,zones,n=1):
    
    """
    return list of all packages name + zones
    """
    
    pack_list=[]
    for i in range(pd.DataFrame(cbc.recordarray).shape[0]-n):
        pack_list.append(str(cbc.recordarray[i+n][-1])[2:5])
    for zm in np.unique(zones):
        if zm != 0:
            pack_list.append("zone {}".format(int(zm)))
    
    return pack_list

def get_Total_Budget(model_name,model_dir):

    """
    Return a DF containing Budget data for the entire model in the LST file
    Only for the 1st time step, 1st stress period for the moment
    model_name : str, name of the model given in the gwf pack
    model_dir : str, path to workspace
    npack : number of additionnal packages with save_flows set True
    """
    
    
    file = "{}/{}.lst".format(model_dir,model_name)
    f = open(file,"r")
    i=-1
    for ilin in f.readlines():
        i += 1
        if ilin =='  VOLUME BUDGET FOR ENTIRE MODEL AT END OF TIME STEP    1, STRESS PERIOD   1\n': # check at which line the budget is
            break
    
    ###number of packages
    npack=0
    for o in range(100):
        f = open("{}/{}.lst".format(model_dir,model_name),"r")
        if f.readlines()[i+8+o]=="\n":
            break
        npack +=1
    ###number of packages
    
    # retrieve data
    lst_val_IN =[]
    lst_val_OUT = []
    lst_nam_pak = []
    pak_type=[]
    for ipak in range(npack):
        ipak += 8
        
        f = open("{}/{}.lst".format(model_dir,model_name),"r")
        lst_nam_pak.append(f.readlines()[i+ipak][85:96].rstrip())

        f = open("{}/{}.lst".format(model_dir,model_name),"r")
        lst_val_IN.append(float(f.readlines()[i+ipak][63:80]))

        f = open("{}/{}.lst".format(model_dir,model_name),"r")
        lst_val_OUT.append(float(f.readlines()[i+ipak+npack+5][63:80]))
        
        f = open("{}/{}.lst".format(model_dir,model_name),"r")
        pak_type.append(f.readlines()[i+ipak][58:62])

    Budget = pd.DataFrame({"Pack":lst_nam_pak,
                  "IN":lst_val_IN,
                 "OUT":lst_val_OUT,
                  "Type":pak_type})

    return Budget