# a master student's hand-made class to handle budget analysis with modflow 6/flopy (Only DIS)

import flopy as fp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

import os


class Zb():
    
    def __init__(self,zones,m_name,m_dir,cbc,m_n=1,dic_zones=None):
        
        # some attributes
        self.nlay = zones.shape[0]
        self.nrow = zones.shape[1]
        self.ncol = zones.shape[2]
        self.m_name = m_name
        self.m_dir = m_dir
        self.n = m_n #this value depends on the save parameters choosed, it must be equal to number of records that aren't from a package (Flow-ja-face, ss storage, spdis, ...). 
        # for ex. If you specify save_specific_discharge = True and save_flows in npf package n will be equal to 2
        
        self.zones = zones
        
        nzones = np.unique(self.zones).shape[0]
        if 0 in np.unique(self.zones):
            nzones -=1
        self.nzones = nzones
        
        #retrieve cbc file

        self.cbc = cbc
        
        #IA and JA arrays
        fname = os.path.join(m_dir, '{}.dis.grb'.format(m_name))
        bgf = fp.utils.mfgrdfile.MfGrdFile(fname)
        self.ia = bgf._datadict['IA'] - 1
        self.ja = bgf._datadict['JA'] - 1
        
        ##df_pos
        self.df_pos = self._df_pos()
        
        self.dz = dic_zones # a dictionnary to give a name on the different zones
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

        for i in range(n,cbc.recordarray.shape[0]):
            for n1,n2,q1 in cbc.get_data(i)[0]:
                zon = int(zones[n1-1])
                if zon != 0:
                    if q1 > 0:
                        pack_flows[i-n,zon*2-2] += q1
                    else:
                        pack_flows[i-n,zon*2-1] -= q1
        
        return pd.DataFrame(pack_flows)

    
    def _index_pack(self):
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
                if not self.dz :
                    pack_list.append("zone {}".format(int(zm)))
                if self.dz :
                    pack_list.append(self.dz[zm])
        return pack_list
############################################
    
    def zones_plot(self):
        
        """
        Plot the different zones of the zone budget object
        """
        zones = self.zones
        nlay = self.nlay
        
        
        fig = plt.figure(figsize=(10,8))
        fig.subplots_adjust(hspace=0.3, wspace=0.1)
        n = math.ceil(nlay**0.5)

        for ilay in range(nlay):
            ax = fig.add_subplot(n, n, ilay+1)
            g = ax.imshow(zones[ilay])
            ax.set_title("layer {}".format(ilay))
            g.set_clim(np.min(zones),np.max(zones))
        cbar_ax = fig.add_axes([0.9, 0.15, 0.05, 0.7])
        fig.colorbar(g,cax=cbar_ax)
    
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
        DF_pack = self._flow_pack(kstpkper=kstpkper) # slow
        
        #append the two dataframes
        df_zz = pd.DataFrame(FluxZZ)
        col = np.arange(0,nzones*2,dtype=int)# use same columns name because pd concat is stupid
        df_zz.columns=col

        DF_Budg = pd.concat([DF_pack,df_zz])# Union <3
        
        #index for the dataframe
        pack_list = self._index_pack()
        
        #create index, multicol, and have fun
        lst_z=[]
        for z in np.unique(zones):
            if z !=0:
                if not self.dz :
                    lst_z.append("zone {}".format(int(z)))
                if self.dz : 
                    lst_z.append(self.dz[z])
        columns = pd.MultiIndex.from_product([lst_z, ['FROM', 'TO']]) 
        index = pack_list
        DF_Budg = pd.DataFrame(DF_Budg.values,index=index,columns=columns)
        
        return DF_Budg
    
    def Z2Z_3D(self,z1,z2,kstpkper=None):

        """
        Total flows from one zone to another

        """
        nlay = self.nlay
        nrow = self.nrow
        ncol = self.ncol
        zones = self.zones.reshape(nlay*nrow*ncol)
        arr = np.zeros([nlay*nrow*ncol])
        flowja = self.cbc.get_data(text='FLOW-JA-FACE',kstpkper=kstpkper)[0][0, 0, :]
        ia = self.ia
        ja = self.ja
        
        
        
        for celln in range(ia.shape[0]-1):
            if zones[celln] == z1:
                for ipos in range(ia[celln]+1, ia[celln+1]): # loop for each connexions of celln
                    cellm = ja[ipos]  # retrieve cell number of adjacent cell
                    if (zones[cellm] == z2): 
                        arr[celln]=flowja[ipos]
        arr[arr==0]=None
        arr = arr.reshape(nlay,nrow,ncol)

        return arr
    
    def return_arr(self,pack,kstpkp=None):
        
        """
        return an array of the flux from a package. Plot sum all the values over each layer.
        
        pack : str, the pname of the package
        cmin/cmax : float, min/max value on the scale
        """
        
        cbc = self.cbc
        nlay = self.nlay
        nrow = self.nrow
        ncol = self.ncol
        
        if type(pack)==str:
            ind = pd.Series(self._index_pack()).loc[pd.Series(self._index_pack())==pack].index
        if type(pack)==int:
            ind = pack
        
        arr3D = cbc.create3D(cbc.get_data(ind+self.n,kstpkper=kstpkp)[0],nlay,nrow,ncol)
        mask = arr3D.mask
        data = arr3D.data
        data = data.sum(axis=0)
        data[data==0]=None
        # a=plt.imshow(data)
        return data