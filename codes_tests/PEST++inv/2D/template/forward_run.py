import os
import multiprocessing as mp
import numpy as np
import pandas as pd
import pyemu
def main():

    try:
       os.remove('.\heads2.csv')
    except Exception as e:
       print('error removing tmp file:.\heads2.csv')

if __name__ == '__main__':
    mp.freeze_support()
    main()

