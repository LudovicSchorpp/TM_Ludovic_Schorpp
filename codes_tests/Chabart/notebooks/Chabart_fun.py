## hand made function for the Chabart model

import numpy as np
import pandas as pd


#1 well data

def pump_data(file,nrow=38,ncol=42,layer=0,fac=1):
    """
    This function take a file (csv) path as entry and spatial parameters (nrow,ncol) and the layer on which the data will be applied
    actually import data from the file in a df, remove value above 3000 and return in a list all the values different from 0 with the appropriate cellid (dis only)
    structure : lst = pump_data(file,nrow,ncol,layer,fac)
    a factor is added in order to change the units of the pumping values, the factor multiply the actual values in the file
    """
    
    lst=[]
    a = pd.read_csv(file,sep=";",header=None,na_values=None)
    a[a>3000] = 0 # remove nodata
    
    for irow in np.arange(nrow):
        for icol in np.arange(ncol):
            if a.iloc[irow,icol] != 0:
                data_pompage = ((layer,irow,icol),a.iloc[irow,icol]*fac)
                lst.append(data_pompage)
    return lst