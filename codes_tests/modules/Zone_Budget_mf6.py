# a master student's hand-made class to handle budget analysis with modflow 6/flopy

import flopy as fp
import numpy as np
import pandas as pd

from Rouss1 import *

#poo tentative
class Zb():
    
    def __init__(self,zones,m_name,m_dir,m_n=1):
        
        # some attributes
        self.nlay = zones.shape[0]
        self.nrow = zones.shape[1]
        self.ncol = zones.shape[2]
        self.m_name = m_name
        self.m_dir = m_dir
        self.n = m_n
        self.zones = zones
        
        nzones = np.unique(self.zones).shape[0]
        if 0 in np.unique(self.zones):
            nzones -=1
        self.nzones = nzones
        
        #retrieve cbc file
        self.cbc = get_cbc(m_name,m_dir)
        
        #IA and JA arrays
        fname = os.path.join(m_dir, '{}.dis.grb'.format(m_name))
        bgf = fp.utils.mfgrdfile.MfGrdFile(fname)
        self.ia = bgf._datadict['IA'] - 1
        self.ja = bgf._datadict['JA'] - 1
        
        ##df_pos
        self.df_pos = self._df_pos()
        
############################################################################################################        
## Methods
    
    def _df_pos(self):
        
        zones = self.zones
        ia = self.ia
        ja = self.ja
        
        def comb(m, lst):
            if m == 0: return [[]]
            return [[x] + suffix for i, x in enumerate(lst)
                    for suffix in comb(m - 1, lst[i + 1:])]
        
        seq=[]
        for zone in np.unique(zones):
            if zone != 0:
                seq.append(int(zone))
        lst_comb = comb(2, seq)

        zones = zones.reshape(self.nlay*self.nrow*self.ncol)
        lst_ipos=[]
        fromz2z=[]

        for zz in lst_comb:
            z1=zz[0]
            z2=zz[1]
            for celln in range(ia.shape[0]-1):
                if zones[celln] == z1:
                    for ipos in range(ia[celln]+1, ia[celln+1]): # loop for each adjacent cells
                        cellm = ja[ipos]  # retrieve cell number of adjacent cell
                        if (zones[cellm] == z2):
                            lst_ipos.append(ipos)
                            fromz2z.append("{}to{}".format(z1,z2))
        df_pos = pd.DataFrame({"ipos":lst_ipos,"dir":fromz2z})
        
        return df_pos
        
    def _flow_zz(self,kstpkper=None):
    
        """
        Return a matrix containing flux btw differents zones (each 2 columns correspond to one zone (1st is IN and 2nd OUT from the zone)
        each layer represent a zone (from zone 1 to zone n)
        cbc : cbc object
        df_pos : Dataframe with infos of connexions btw interzones cells (see get_dfpos)
        zones : the numpy 3D array with the zones
        kstpkper : array of size 2, indices that indicates stress period and time step
        """
        cbc = self.cbc
        zones = self.zones
        df_pos = self.df_pos
        nzones = self.nzones
        
        flowja = cbc.get_data(text='FLOW-JA-FACE',kstpkper=kstpkper)[0][0, 0, :]
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
    
    def _flow_pack(self,kstpkper=None):
        
        nlay = self.nlay
        nrow = self.nrow
        ncol = self.ncol
        zones = self.zones.reshape(nlay*nrow*ncol)
        nzones = self.nzones
        n = self.n
        cbc = self.cbc
        
        pack_flows = np.zeros([cbc.recordarray.shape[0]-n,nzones*2])

        for i in range(1,cbc.recordarray.shape[0]):
            for n1,n2,q1 in cbc.get_data(i)[0]:
                zon = int(zones[n1-1])
                if zon != 0:
                    if q1 > 0:
                        pack_flows[i-1,zon*2-2] += q1
                    else:
                        pack_flows[i-1,zon*2-1] -= q1
        
        return pd.DataFrame(pack_flows)

    
    def index_pack(self):
        """
        return list of all packages name + zones
        """
        cbc = self.cbc
        zones = self.zones
        pack_list=[]

        for i in range(pd.DataFrame(cbc.recordarray).shape[0]-self.n):
            pack_list.append(str(cbc.recordarray[i+self.n][-1])[2:17].strip())
        for zm in np.unique(zones):
            if zm != 0:
                pack_list.append("zone {}".format(int(zm)))

        return pack_list
############################################

    def get_Budget(self,kstpkper=None):
        
        
        """
        Return a table with budget at a certain time step
        """
        
        cbc = self.cbc
        zones = self.zones
        df_pos = self.df_pos
        nzones = self.nzones
        
        FluxZZ = self._flow_zz(kstpkper=kstpkper)
        
        # total budgets for 1st stress period
        DF_pack = self._flow_pack(kstpkper=kstpkper) # slow... need to fix it
        
        #append the two dataframes
        df_zz = pd.DataFrame(FluxZZ)
        #col = np.zeros(nzones*2,dtype=int) # use same columns name because pd concat is stupid
        col = np.arange(0,nzones*2,dtype=int)# use same columns name because pd concat is stupid
        df_zz.columns=col

        DF_Budg = pd.concat([DF_pack,df_zz])# Union <3
        
        #index for the dataframe
        pack_list = self._index_pack()
        
        #create index, multicol, and have fun
        lst_z=[]
        for z in np.unique(zones):
            if z !=0:
                lst_z.append("zone {}".format(int(z)))
        columns = pd.MultiIndex.from_product([lst_z, ['FROM', 'TO']]) 
        index = pack_list
        DF_Budg = pd.DataFrame(DF_Budg.values,index=index,columns=columns)
        
        return DF_Budg
    