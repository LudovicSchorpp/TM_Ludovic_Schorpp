#list of functions that helps with parametrization and setup PEST ++ from MODFLOW 6

import flopy as fp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#1
def list2txt(liste,filename,ncol=2,nid=3):
    
    """
    Transform a python list for flopy into a txt file that can be open from modflow files
    liste : the flopy stress period data list (cellid, var1,var2, ...)
    filename : filename of the new txt file
    ncol : number of column in the list (cellid count as one column even there's 3 numbers (DIS f.ex))
    nid : number of elements that defines cell id (1, 2 or 3)
    """
    
    with open(filename,"w") as f:
        for ob in liste:
            for i in range(nid): # loop for cellid
                f.write(" "+ str(ob[0][i]))
            for icol in range(1,ncol): # loop for each column of the list
                f.write("   " + str(ob[icol]))
            f.write("\n")