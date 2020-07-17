import os
import multiprocessing as mp
import numpy as np
import pandas as pd
import pyemu
def main():

    try:
       os.remove('.\heads_q.csv')
    except Exception as e:
       print('error removing tmp file:.\heads_q.csv')
    try:
       os.remove('.\heads_pc.csv')
    except Exception as e:
       print('error removing tmp file:.\heads_pc.csv')

if __name__ == '__main__':
    mp.freeze_support()
    main()

