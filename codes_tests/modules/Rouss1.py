# some useful "hand-made" functions

import flopy as fp
import numpy as np
import geopandas as gp
import pandas as pd
import os
import gdal
import matplotlib.pyplot as plt
from flopy.utils.gridgen import Gridgen 
from flopy.utils.gridintersect import GridIntersect
import shapely
from shapely.geometry import Polygon, Point, LineString, MultiLineString, MultiPoint, MultiPolygon
from shapely.strtree import STRtree  


#1
def Imreduction (imar, nrow, ncol):
    
    """
    This function reduce the dimensionality of an image.
    An array of the image must be provided by the user, same for the number of row and col of the new image
    No data should be specified as "None" type
    return a new array
    """
    
    #first define the ratio between the given and the desired resolution in x and y
    facR=imar.shape[0]/nrow
    facC=imar.shape[1]/ncol
    
    # go through the entire grid (nrow,ncol) and use the mean of all the values in the array image
    # in a specific cell of the grid (i,o)
    new_imar=[]
    for i in range(nrow):
        for o in range(ncol):
            new_val=np.nanmean(imar[np.round(i*facR).astype(int):np.round(i*facR+facR).astype(int),
                                    np.round(o*facC).astype(int):np.round(o*facC+facC).astype(int)])
            new_imar.append(new_val)
    
    # create an array of the new image array
    new_imar = np.array(new_imar)
    return np.array(pd.DataFrame(new_imar.reshape(nrow,ncol)).fillna(0))


#2
def gp2idomain (gp,grid,idomain,area=0,layer=0,method="none"):
    
    '''
    This function attribute active values to cells given a certain geopandas object and a grid (flopy.discretization) with idomain
    the area is a value that determine at which level a cell will be counted as intersected by the polygon 
    (3 for example mean that only cells that have 1/3 of their area intersected by the polygon will be accounted)
    '''
    if method == "none":
        ix = GridIntersect(grid)
    if method == "structured":
        ix = GridIntersect(grid,method=method)
    
    if area == 0:
        result = ix.intersect_polygon(gp.geometry[0])
    
    if area >= 1:
        result = ix.intersect_polygon(gp.geometry[0])
        result = result[result.areas>(np.max(result.areas)/area)]
        
    lst=[]
    result = result[result.areas!=0]
    for irow, icol in result.cellids:
        idomain[irow*grid.ncol+icol]=1
        lst.append(((layer,irow,icol)))
    return lst



#3
def gp2cellids (grid, gp, idomain, idomain_active=True, type = "polygon",layer=0,areas=3):
    """
    this function extract the cellids of the intersection between a geopandas object and a grid 
    grid : modelgrid
    gp : geopandas object (polygon, linestring only)
    idomain : the idomain array to update it
    idomain_active : bool, if true the idomain is update (cells intersect by the gp will be noted as active), prevents some issues
    type : str, features type (polygon or line)
    layer : int, the layer on which is the gp
    areas : factor that determine if a cell is accounted intersected or not based on the total area intersected in this cell 
    (a value of 3, for example, mean only cells which have 1/3 of their area intersected by the polygon will be taken into account)
    """
    
    ix = GridIntersect(grid)
    if type == "polygon":
        result = ix.intersect_polygon(gp.geometry[0])
        result = result[result.areas>(np.max(result.areas)/3)] # only take into account cells that have a least 1/3 intersected 
        result = result[result.areas!=0]                       # fix bug
        
    if type == "boundary" :
        result = ix.intersect_linestring(gp.geometry[0].boundary)

        
    if type == "line" :
        result = ix.intersect_linestring(gp.geometry[0])
        
    lst=[]
    
    for irow, icol in result.cellids:
        lst.append(((layer,irow,icol)))
        if idomain_active:
            idomain[irow*grid.ncol+icol] = 1
    return lst



#4
def cellidBD(idomain, layer=0):   
    
    """
    extract the cellids at the boundary of the domain at a given layer
    """
    lst_cellBD=[]

    for irow in range(idomain.shape[1]):
        for icol in range(idomain.shape[2]):
            if idomain[layer][irow,icol]==1:
                #check neighbours
                if np.sum(idomain[layer][irow-1:irow+2,icol-1:icol+2]==1) < 8:
                    lst_cellBD.append((layer,irow,icol))
    return lst_cellBD


# 5 visualization functions
def get_heads(model_name,workspace,obj=False):
    """
    Function that returns the heads from the headfile
    model_name : str, the name of the current model
    workspace : str, the path to workspace (where output files are stored)
    obj : bool, if we want to have the head object rather than the computed heads for the last stress period
    """
    headfile = '{}.hds'.format(model_name)
    fname = os.path.join(workspace,headfile)    
    hdobj = fp.utils.HeadFile(fname, precision='double') 
    
    head  = hdobj.get_data()
    
    if obj:
        return hdobj
    else:
        return head



def get_spdis(model_name,workspace):
    """
    Function that returns the specific discharge from the cbcfile
    """
    spdfile = '{}.cbc'.format(model_name)
    fname = os.path.join(workspace,spdfile)    
    spdobj = fp.utils.CellBudgetFile(fname, precision='double')  
    spd  = spdobj.get_data(text="SPDIS")
    return spd

def get_cbc(model_name,workspace):
    cbcfile = '{}.cbc'.format(model_name)
    fname = os.path.join(workspace,cbcfile)    
    cbcobj = fp.utils.CellBudgetFile(fname, precision='double')  
    return cbcobj

def get_budgetobj(model_name,workspace):
    """
    Function that returns the budget file as an object
    """
    lstBudgetfile = "{}.lst".format(model_name)
    fname = os.path.join(workspace,lstBudgetfile)
    Budgetobj = fp.utils.Mf6ListBudget(fname)
    return Bugetobj


#6
def get_MNTbbox (MNT_path):
    """
    Function that returns the x0,y0,x1 and y1 (in this order) of a mnt in the mnt's Coord. Sys.
    """
    
    R_mnt = gdal.Open(MNT_path)
    mnt_infos=R_mnt.GetGeoTransform()
    x0 = mnt_infos[0]+mnt_infos[1]/2
    x1 = x0 + R_mnt.RasterXSize*mnt_infos[1]
    y1 = mnt_infos[3]+mnt_infos[5]/2
    y0 = y1 + R_mnt.RasterYSize*mnt_infos[5]
    
    return x0,y0,x1,y1


#7
def inter_lst (lst1,lst2,typ = "intersection"):
    """
    return the intersection/unique values of the list1 compared to list2
    """
    
    if typ == "intersection":
        return [i for i in lst1 if i in lst2]
    if typ == "unique":
        return [i for i in lst1 if i not in lst2]
        
#8
def import_riv(grid,gp,lst_domain,nlay=3):
    
    """
    This function extract infos about a river (geopandas object, LINESTRING),cellids + lengths of in each cells in the right order. 
    Format : 
    import_riv (Grid (from the gwf model, gwf.modelgrid for ex.)
    
    gp (a geopandas object containing a unique Linestring))
    
    Return a dataframe containing these datas, post-processing necessary to remove cells that are already counted as BC in the model
    """
    
    ix = GridIntersect(grid)
    coord_riv=[]
    for x,y in zip(gp.geometry[0].xy[0],gp.geometry[0].xy[1]):
        coord_riv.append((x,y))

    verti=[]
    df_tot_ord = pd.DataFrame() # empty DF
    for i in range(len(coord_riv)):
        if i < len(coord_riv)-1:
            lsi = LineString([coord_riv[i],coord_riv[i+1]]) # create the linestring btw point i and i+1
            res = ix.intersect_linestring(lsi) # do the intersection
            res = res[res["lengths"]!=0] # remove a bug issue on Linux
            cellids = res.cellids # extract cellids

            if len(cellids)>1: # if more than one cells is intersected --> we need to order them

                dirx = coord_riv[i+1][0]-coord_riv[i][0] # Xdirection of the linestring

                for x,y in res.vertices: # extract the 1st vertice of the intersections in order to organize the cells
                    verti.append(x)
                vertix = np.array(verti)[:,0]
                df = pd.DataFrame({"cellids":cellids,"vertix":vertix,"lengths":res.lengths}) # create a DF to order
                verti=[]

                #organize the cells given the direction
                if dirx > 0:
                    df.sort_values(by=["vertix"],ascending=True,inplace=True)                
                if dirx < 0:
                    df.sort_values(by=["vertix"],ascending=False,inplace=True) 

                # append these data in a big DF
                df_tot_ord = df_tot_ord.append(df).drop(["vertix"],axis=1)

            else : # if only one cell is intersected by the linestring
                df_tot_ord = df_tot_ord.append(pd.DataFrame({"cellids":cellids,"lengths":res.lengths}))

    df_riv = df_tot_ord.groupby(["cellids"],sort=False).sum()

    # retrieve data
    lst_len_Riv = df_riv["lengths"].values

    cellids_Riv=[]; # list of all the cells intersected by the river
    cellids = df_riv.index
    for irow,icol in cellids:
        for layer in range(nlay):
            cell = (layer,irow,icol)
            if cell in lst_domain: #attribute the river to the uppermost active cell
                break
        if cell not in cellids_Riv:
            cellids_Riv.append(cell)

    df_riv = pd.DataFrame({"cellids":cellids_Riv,"lengths":lst_len_Riv})       
    return df_riv
    

#9
def get_cellcenters (grid,cellids): 
    """
    This function return the x and y coordinates of a given cellid and a grid (dis only)
    """
    xc=[];yc=[]
    
    for i,j,k in cellids:
        xc.append(grid.xcellcenters[j,k])
        yc.append(grid.ycellcenters[j,k])
    return xc,yc


#10
def lin_interp(lengths,Hv,Lv):
    """
    function that realize a linear interpolation btw 2 values, given a certain weighting list (lengths typically for a river)
    """
    
    ar_long = np.array(lengths)
    dh_dl = (Lv-Hv)/lengths.sum()
    H_riv = np.zeros(ar_long.shape[0],dtype=np.float)    
    for idx in range(ar_long.shape[0]):
        if idx == 0:
            len_cum = 0.5 * ar_long[0]
        else:
            len_cum += 0.5 * (ar_long[idx-1]+ar_long[idx])
        H_riv[idx] = Hv + len_cum * dh_dl
    return H_riv


#11 
def linInt_Dfcol(df,weight="lengths",col="head",null=0):
    
    """
    function that linearly interpolates the values in a column btwn certains given values (not null), a null value is indicated by 0
    this function needs the lin_interp function, a weighting factor must be provided and a column in the df.
    df : a dataframe
    weight : a column of the same size that the interpolated column (default : "head") which is used as a weight
    col : the interpolated column (null value = 0)
    """
    
    new_heads=np.zeros([df.shape[0]])
    for i in np.arange(df[df[col]!=null].index.shape[0]-1):
        idx1 = df[df[col]!=null].index[i]
        idx2 = df[df[col]!=null].index[i+1]
        new_heads[idx1:idx2+1] = lin_interp(df[weight][idx1:idx2+1],df[col][idx1],df[col][idx2])
    df[col]=new_heads
    

#12
def ra_pack(pack,ibd,iper=0):
    
    """
    Return recarray containing position of cells from a certain package
    Can be used to plot the bc zones of a certain package (pack), iper is for the period
    """
    
    ra = pack.stress_period_data.get_data(key=iper)
    for k, i, j in ra['cellid']:
        ibd[k, i, j] = -1
        
        
#13
def importControlPz (file_path,grid,sheetName="1990",np_col = "NP",x_col="x",y_col="y"):
    
    """
    return an array containing infos about piezometer level in control pz
    file_path : the file path to the excel sheet
    sheetName : the name of the data sheet 
    np_col : the name of the column containing infos about the PL
    x_col,y_col : the name of the columns containings geo infos
    """
    
    DB = pd.read_excel(file_path,sheet_name = sheetName) # read the file with pandas
    
    Control_pz = np.zeros([grid.nrow,grid.ncol]) #ini list
    lstIDpz=[];Pz = [];
    
    for o in np.arange(DB.shape[0]): # loop to iterate through the data and returns the intersected cellids
        xc = DB["x"][o]
        yc = DB["y"][o] 
        cellid = grid.intersect(xc,yc)
        
        if not np.isnan(DB[np_col][o]):
            lstIDpz.append(cellid)
            Pz.append(DB[np_col][o])
        
    df = pd.DataFrame()
    df["cellid"]=lstIDpz
    df["Pz"] = Pz
    df = df.groupby(["cellid"]).mean().reset_index()
    
    for i in df.index:
        j,k = df.loc[i,"cellid"]
        Control_pz[j,k] = df.loc[i,"Pz"]
    
    return Control_pz


#14
def importWells(path,grid,lst_domain,fac=1/365/86400,V_col="V Bancaris",layer=0):
    
    """
    extract the infos about the uptake of water in wells
    path : path to the shp (multi points required)
    grid : the modelgrid
    fac : the factor to apply on the Volume to get m3/s
    V_col : the column name containing info about Volume
    layer : the layer on which the wells are active
    """
    
    GDB = gp.read_file(path)
    stress_data_well=[]
    ix = GridIntersect(grid)

    for o in GDB.index:
        Vw = GDB[V_col][o]
        if not (np.isnan(Vw)) | (Vw == 0):
            try:
                cellidx = ix.intersect_point(GDB.geometry[o]).cellids[0][0]
                cellidy = ix.intersect_point(GDB.geometry[o]).cellids[0][1]
                cellid = (layer,cellidx,cellidy)
                if cellid in lst_domain:
                    stress_data_well.append((cellid,-fac*Vw))
            except:
                pass

    return stress_data_well

#15
def coor_convert(x,y,epsgin,epsgout):
    
    """
    a function that converts coordinates, needs coordinates and epsgin and epsgout.
    """
    from pyproj import Proj, transform
    inproj = Proj(init="epsg:{}".format(epsgin))
    outproj = Proj(init="epsg:{}".format(epsgout))
    xp,yp = transform(inproj,outproj,x,y)
    return xp,yp


#16 
def Chabart2df(file):
    
    """
    to import data from a Chabart files (csv file), return a df with coordinates and the values in L93
    """
    
    x_l=[]; y_l=[]; V=[]
    x0 = 620;y1 = 3062;
    data = pd.read_csv(file,sep=";",header=None,na_values=None)
    data[data==7777]=0 # remove nodata
    data[data==9999]=0 # remove nodata
    nrow=38;ncol=42


    for irow in np.arange(nrow):
        if irow == 0:
            y = y1
        else:
            y = y1 - irow
        for icol in np.arange(ncol):
            if icol == 0 :
                x = x0
            else:
                x = x0 + icol
            if data.iloc[irow,icol] != 0:
                x_l.append(x)
                y_l.append(y)
                V.append(data.iloc[irow,icol])
    
    x_l = [i*1000 for i in x_l]
    y_l = [i*1000 for i in y_l]
    X,Y = coor_convert(x_l,y_l,27573,2154)
    return pd.DataFrame({"x":X,"y":Y,"data":V})


#16 bis 
def dfXY2lstModflow(df,x_col="x",y_col="y",data_col="data",layer=0,fac=1/1000/365/86400):
    
    """
    from a df with x,y and data to a Modflow list with cellids and stuffs, in progress...
    can be used easily with Chabart2lst
    """
    lst = []
    for i in range(len(a)):
        x = a.loc[i,"x"]
        y = a.loc[i,"y"]
        cellidr,cellidc = grid.intersect(x,y)
        lst.append(((layer,cellidr,cellidc),fac*a.loc[i,"data"]))
    return lst


#17
def chd2riv(riv_chd,cond,rdepth):
    
    """
    Transform a chd stress period data into a riv stress period data
    riv_chd : list, chd spd (cellid,stage)
    cond : float, conducance of the riverbed
    rdepth : float, depth of the river
    """
    
    Riv=[]
    for cellid,stage in riv_chd:
        Riv.append((cellid,stage,cond,stage-rdepth))
    
    riv_chd[:] = Riv
    
#18
def nn2kij(n,nlay,nrow,ncol):
    """
    from a node number to ilay,irow and icol (dis)
    """
    return fp.utils.gridintersect.ModflowGridIndices.kij_from_nn0(n,nlay,nrow,ncol)

#19
def budg(budg_data):
    
    """
    return in and out budget info from a package of the model
    budg_data : data from the cbc object of modflow for one package
    example : budg(cbc.get_data[idx = 0])
    """
    pos=0
    neg=0
    for i in budg_data:
        for o,j,k in i:
            if k >0:
                pos += k
            else:
                neg -= k
    return pos,neg