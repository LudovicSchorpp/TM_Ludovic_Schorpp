#list of functions that helps with parametrization and setup PEST ++ from MODFLOW 6
import os
import sys
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
                f.write(" "+ str(ob[0][i]+1))
            for icol in range(1,ncol): # loop for each column of the list
                f.write("   " + str(ob[icol]))
            f.write("\n")
            
#2            
def pack2txt(fname,txt_file):
    
    """
    Function that extract list based stress data from a flopy package (riv, rch, ...) 
    and write it to a external txt file. The package is thus change in order to call the txt file as input
    Can be useful for inversion and pest setup.
    fname : path to flopy package
    txt_file : path of the new txt file
    
    Works for a steady model with stress period 1
    Multiple stress periods TODO !
    """
    
    fname
    tmp_f = "tmp"
    i_write=1
    with open(txt_file,"w") as t:
        with open(fname) as f:
            with open(tmp_f,"w") as f2:
                lines = f.readlines()
                for i in range(len(lines)): # loop over lines
                    if lines[i] == 'END period  1\n': # if line is END period 1, rewrite
                        i_write=1
                    if i_write:
                        f2.write(lines[i]) #write new riv file
                    if not i_write:
                        t.write(lines[i]) #write txt file (data)
                    if lines[i] == 'BEGIN period  1\n':
                        i_write=0
                        f2.write("OPEN/CLOSE    '{}'  FACTOR  1.0\n".format(txt_file.split("\\")[-1]))
    
    from shutil import copyfile
    copyfile(tmp_f, fname) # copy 
    os.remove(tmp_f) # delete tmp file