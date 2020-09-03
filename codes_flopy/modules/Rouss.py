import flopy as fp
import numpy as np
import geopandas as gp
import pandas as pd
import os
import matplotlib.pyplot as plt
from flopy.utils.gridgen import Gridgen 
from flopy.utils.gridintersect import GridIntersect
from flopy.utils import Raster
import shapely
from shapely.geometry import Polygon, Point, LineString, MultiLineString, MultiPoint, MultiPolygon
from shapely.strtree import STRtree  

#1
def gp2cellids (grid, gp, idomain, idomain_active=True, type = "polygon",layer=0,areas=3):
    
    """
    this function extract the cellids of the intersection between a geopandas object and a grid 
    grid : modelgrid with flopy.discretisation !
    gp : geopandas object with one entity only
    idomain : array, the idomain array to update it
    idomain_active : bool, if true the idomain is update (cells intersect by the gp will be noted as active), prevents some issues
    type : str, features type (polygon or line)
    layer : int, the layer on which is the gp
    areas : factor that determine if a cell is accounted as intersected or not based on the total area intersected
    (a value of 3, for example, means only cells which have 1/3 of their area intersected by the polygon will be taken into account)
    """
    
    ix = GridIntersect(grid)
    if type == "polygon":
        result = ix.intersect_polygon(gp.geometry[0])
        result = result[result.areas>(np.nanmax(result.areas)/3)] # only take into account cells that have a least 1/3 intersected 
        
        
    if type == "boundary" :
        result = ix.intersect_linestring(gp.geometry[0].boundary)
        
    if type == "line" :
        result = ix.intersect_linestring(gp.geometry[0])
        
    result = result[result.areas!=0]                       # fix bug with some null areas
    
    lst=[]
    for irow, icol in result.cellids:
        lst.append(((layer,irow,icol)))
        if idomain_active:
            idomain[irow*grid.ncol+icol] = 1
    return lst

#2
def cellidBD(idomain, layer=0):   
    
    """
    extract the cellids at the boundary of the domain at a given layer
    idomain : 3D array, idomain array which determine if a cell is active or not (1 active, 0 inactive)
    layer : int, layer on which the boundary cells are extract
    """
    lst_cellBD=[]

    for irow in range(idomain.shape[1]):
        for icol in range(idomain.shape[2]):
            if idomain[layer][irow,icol]==1:
                #check neighbours
                if np.sum(idomain[layer][irow-1:irow+2,icol-1:icol+2]==1) < 8:
                    lst_cellBD.append((layer,irow,icol))
    return lst_cellBD


#3 get functions
def get_heads(model_name,workspace,obj=False):
    """
    Function that returns the heads from the headfile
    model_name : str, the name of the current model
    workspace : str, the path to workspace (where output files are stored)
    obj : bool, if we want to retrieve the head object rather than the computed heads for the last stress period
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


#4
def inter_lst (lst1,lst2,typ = "intersection"):
    
    """
    return the intersection/unique values of the list1 compared to list2
    lst1 and lst2 : list
    typ : type of comparison (intersection or unique)
    """
    
    if typ == "intersection":
        return [i for i in lst1 if i in lst2]
    if typ == "unique":
        return [i for i in lst1 if i not in lst2]

#5  
def import_riv(grid,gp,lst_domain):
    
    """
    This function extract infos about a river (geopandas object, LINESTRING),cellids + lengths of in each cells in the right order. 
    Format : 
    
    grid : from the gwf model, gwf.modelgrid for ex. or flopy.discretisation)
    gp : a geopandas object containing a single Linestring(which can have multiple segements however)
    lst_domain : list of all active cells

    Return a dataframe containing these datas, post-processing necessary to remove cells that are already counted as BC in the model
    """
    
    nlay = np.max(np.array(lst_domain)[:,0])+1 #nlay
    
    ix = GridIntersect(grid)
    coord_riv=[]
    for x,y in zip(gp.geometry[0].xy[0],gp.geometry[0].xy[1]): # extract river coord
        coord_riv.append((x,y))

    verti=[]
    df_tot_ord = pd.DataFrame() # empty DF
    for i in range(len(coord_riv)):
        if i < len(coord_riv)-1:
            lsi = LineString([coord_riv[i],coord_riv[i+1]]) # create the linestring btw point i and i+1
            res = ix.intersect_linestring(lsi) # do the intersection
            res = res[res["lengths"]!=0] # remove a bug issue on Linux with lengths == 0
            cellids = res.cellids # extract cellids (row,col, only)

            if len(cellids)>1: # if more than one cells is intersected --> we need to order them

                dirx = coord_riv[i+1][0]-coord_riv[i][0] # variation of x (to know if the segment go to right or left)

                for x,y in res.vertices: 
                    verti.append(x)
                vertix = np.array(verti)[:,0] # extract the 1st vertice of the intersections in order to organize the cells
                df = pd.DataFrame({"cellids":cellids,"vertix":vertix,"lengths":res.lengths}) # create a temp DF to order
                verti=[]

                #organize the cells given the direction
                if dirx > 0:
                    df.sort_values(by=["vertix"],ascending=True,inplace=True)                
                if dirx < 0:
                    df.sort_values(by=["vertix"],ascending=False,inplace=True) 

                # append these data in a big DF
                df_tot_ord = df_tot_ord.append(df,sort=True).drop(["vertix"],axis=1)

            else : # if only one cell is intersected by the linestring
                df_tot_ord = df_tot_ord.append(pd.DataFrame({"cellids":cellids,"lengths":res.lengths}))

    df_riv = df_tot_ord.groupby(["cellids"],sort=False).sum() # regroup river within the same cells and sum the lengths

    # retrieve data
    lst_len_Riv = df_riv["lengths"].values

    # attribute on which layer these cells are active
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

    
#6
def Complete_riv(riv_path,stations_csv,us,ds,lst_chd,lst_domain,grid):
    
    """
    a complete function that import a river and return the stress data.
    the river path, the station path and the upstream and downstream head as number of layers must be provided
    
    riv_path : the path to the shapefile of the river (one linestring only)
    stations_csv : path to the csv file containing the infos about the stations (x,y,elevation)
    lst_chd : a list of every cells constant heads
    lst_domain : a list of each active cell
    grid : grid of the model
    """
    
    BC_riv = gp.read_file(riv_path) # read shp, linestring from ups to dws
    df_riv = import_riv(grid,BC_riv,lst_domain) # extract cellids intersected + lengths in each cells
    df_riv["xc"],df_riv["yc"] = get_cellcenters(grid,df_riv.cellids)
    df_riv["head"] = np.zeros([df_riv.shape[0]]) # create a new column for the heads

    # us and ds heads
    df_riv.loc[0,"head"] = us
    df_riv.loc[df_riv.index[-1],"head"] = ds
    
    # ref points and assignement of heads
    riv_stations = pd.read_csv(stations_csv,sep=";")
    for i in riv_stations.index:
        xs = riv_stations.loc[i].x
        ys = riv_stations.loc[i].y
        elev = riv_stations.loc[i].elev
        dist = ((df_riv["xc"] - xs)**2 + (df_riv["yc"] - ys)**2)**0.5
        df_riv.loc[dist==np.min(dist),"head"] = elev

    # interpolation of the heads btw ups,stations and ds
    # linInt_Dfcol(df_riv,col="head")
    
    # length cumulated
    lcm=0
    l_cum=[]
    for l in df_riv.lengths:
        lcm += l/2
        l_cum.append(lcm)
        lcm += l/2
    df_riv["l_cum"] = l_cum
    
    # linear interp (0 as a null value)
    yp = df_riv["head"][df_riv["head"]!=0]
    xp = df_riv["l_cum"][df_riv["head"]!=0]
    df_riv["head"] = np.interp(df_riv["l_cum"],xp,yp)
    
    # drop cells outside domain or already chd
    for cellid in df_riv.cellids:
        if (cellid in lst_chd) | (cellid not in lst_domain): 
            df_riv = df_riv.drop(df_riv[df_riv["cellids"] == cellid].index)
    
    # create the stress package
    df_riv= df_riv.reset_index()
    H_riv = df_riv["head"]
    riv_chd=[]; o =-1;
    for x in df_riv.cellids:
        o = o + 1
        riv_chd.append((x,H_riv[o]))
        lst_chd.append(x) # update chd list
    return riv_chd


#7
def get_cellcenters (grid,cellids): 
    """
    This function return the x and y coordinates of a given cellid and a grid (dis only)
    """
    xc=[];yc=[]
    
    for i,j,k in cellids:
        xc.append(grid.xcellcenters[j,k])
        yc.append(grid.ycellcenters[j,k])
    return xc,yc
    
#8
def ra_pack(pack,ibd,iper=0,value=-1):
    
    """
    Return an array containing position of cells from a certain package
    Can be used to plot the bc zones of a certain package (pack)
    pack : a bc package which possess a stress_period_data attribute
    ibd : 3D array on which the value will be change 
    iper : int, stress period
    value : int, value of replacement in ibd
    """
    
    ra = pack.stress_period_data.get_data(key=iper)
    for k, i, j in ra['cellid']:
        ibd[k, i, j] = value 

#9
def importControlPz (file_path,grid,sheetName="1990",np_col = "NP",x_col="x",y_col="y"):
    
    """
    For 2D models ! 
    return an array (nrow,ncol) containing infos about pz observations in control pz
    file_path : the file path to the excel sheet
    grid : modelgrid (flopy.discretization.structuredgrid object)
    sheetName : the name of the data sheet 
    np_col : the name of the column in the file containing infos about the PL
    x_col,y_col : the name of the columns containings geo infos (x and y coordinates)
    """
    
    DB = pd.read_excel(file_path,sheet_name = sheetName) # read the file with pandas
    
    Control_pz = np.zeros([grid.nrow,grid.ncol]) #ini list
    lstIDpz=[];Pz = [];
    
    for o in np.arange(DB.shape[0]): # loop to iterate through the data and returns the intersected cellids
        xc = DB["x"][o]
        yc = DB["y"][o] 
        cellid = grid.intersect(xc,yc)
        
        if DB[np_col][o]: # check that a head data is available
            lstIDpz.append(cellid) # list of cellids
            Pz.append(DB[np_col][o]) # list of value
        
    df = pd.DataFrame()
    df["cellid"]=lstIDpz
    df["Pz"] = Pz
    df = df.groupby(["cellid"]).mean().reset_index() # regroup pz in the same cells and apply mean
    
    #create the obs array
    for i in df.index:
        j,k = df.loc[i,"cellid"] #extract cellids
        Control_pz[j,k] = df.loc[i,"Pz"] # change pz value
    
    return Control_pz

#10
def importWells(GDB,grid,lst_domain,fac=1/365/86400,V_col="V Bancaris",layer=0):
    
    """
    2D only !
    extract the infos about the uptake of wells
    path : path to the shp (multi points required)
    grid : the modelgrid
    fac : the factor to apply on the Volume to get m3/s
    V_col : the column name containing info about Volume
    layer : the layer on which the wells are active
    """
    

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

#11
def coor_convert(x,y,epsgin,epsgout):
    
    """
    Function that converts coordinates
    x,y : coordinates from epsgin
    epsgin : actual epsg system 
    epsgout : the epsg goal
    """
    
    from pyproj import Proj, transform
    inproj = Proj(init="epsg:{}".format(epsgin))
    outproj = Proj(init="epsg:{}".format(epsgout))
    xp,yp = transform(inproj,outproj,x,y)
    return xp,yp

#12
def chd2riv(riv_chd,cond,rdepth,stage_var=1):
    
    """
    Transform a chd stress period data into a riv stress period data
    riv_chd : list, chd spd (cellid,stage)
    cond : float, conducance of the riverbed
    rdepth : float, depth of the river botom (from the stage)
    """
    
    Riv=[]
    for cellid,stage in riv_chd:
        Riv.append((cellid,(stage-rdepth)+rdepth*stage_var,cond,stage-rdepth))
    riv_chd[:] = Riv

#13
def nn2kij(n,nlay,nrow,ncol):
    
    """
    from a node number to ilay,irow and icol (dis)
    """
    
    return fp.utils.gridintersect.ModflowGridIndices.kij_from_nn0(n,nlay,nrow,ncol)

#14
def get_Total_Budget(model_name,model_dir,kstpkper=(0,0)):

    """
    Return a DF containing Budget data for the entire model by searching in the LST file. Budget should have been Printed in Output Control
    model_name : str, name of the model given in the gwf pack
    model_dir : str, path to workspace
    """
    
    file = os.path.join(model_dir,"{}.lst".format(model_name))   
    with open(file) as f:
        doc = f.readlines()
    i=-1
    tmstp=0;sp=0;inf=0
    for ilin in doc: # iterate through lines
        i += 1 # idx line
        info=""
        try:
            tmstp = int(ilin[52:58].split(",")[0])
            sp = int(ilin[73:-1])
            info = ilin[2:15]
        except:
            pass
        if (info == "VOLUME BUDGET") & (tmstp == kstpkper[0]+1) & (sp == kstpkper[1]+1): #if this line is encountered --> break
            break
    
    if i == len(doc):
        raise Exception ("No Budget info found ! Check Output Control or stress period ")
    
    ###number of packages
    npack=0
    for o in range(1000):
        if doc[i+8+o]=="\n":
            break
        npack += 1
    ###number of packages
    
    # retrieve data
    lst_val_IN =[]
    lst_val_OUT = []
    lst_nam_pak = []
    pak_type=[]
    for ipak in range(npack): # ipak --> line indice for a specific package
        ipak += 8 # packages begin 8 lines after i

        lst_nam_pak.append(doc[i+ipak][85:96].rstrip()) # Package name
        lst_val_IN.append(float(doc[i+ipak][63:80])) # value IN
        lst_val_OUT.append(float(doc[i+ipak+npack+5][63:80])) # Value OUT
        pak_type.append(doc[i+ipak][55:62]) # Package type

    Budget = pd.DataFrame({"Pack":lst_nam_pak,
                  "IN":lst_val_IN,
                 "OUT":lst_val_OUT,
                  "Type":pak_type})

    return Budget

#15
def arr2ascii(arr,filename,x0,y0,res,nodata=-9999):
    
    """
    Create an ascii raster file from an array as a base. Left corner origin and resolution must be provided.
    arr : 2D numpy arr
    filename : the path/name for the new ascii file
    x0,y0 : left corner origin of the array
    res : Ascii resolution
    nodata : no data value
    """
    
    ncol = arr.shape[1]
    nrow = arr.shape[0]
    with open(filename,"w") as file:
        file.write("ncols {}\n".format(ncol))
        file.write("nrows {}\n".format(nrow))
        file.write("xllcorner {}\n".format(x0))
        file.write("yllcorner {}\n".format(y0))
        file.write("cellsize {}\n".format(res))
        file.write("nodata_value {}\n".format(nodata))
        for irow in range(nrow):
            for icol in range(ncol):
                file.write(str(arr[irow,icol])+" ")

#16
def rspl_rast(rast_path,grid,band=1):
    
    """
    Use the resample_to_grid method from flopy Raster. 
    rast_path : path to the raster
    grid : modelgrid (gwf.modelgrid or flopy.discretisation)
    """
    
    rast = Raster.load(rast_path)
    arr = rast.resample_to_grid(grid.xcellcenters,grid.ycellcenters,band)
    return arr

#17
def k_zones(k,z1,layer,kn,ix): 
    
    """
    Change value in a numpy 3D array location based on a certain zone (format: [(x1,y1),(x2,y2), ...])
    Design for update permeability array but can be used for any other purpose that imply modifying an array in a specific zone
    
    z1: list of tuples, zone (format: [(x1,y1),(x2,y2), ...])
    layer : list or int, layers on which to apply changes
    kn : float, the new value of k
    ix : gridintersect object --> ix = GridIntersect(grid) as grid the modelgrid
    """
    
    poly = Polygon(z1)
    res = ix.intersect_polygon(poly)
    if type(layer) != int:
        for ilay in layer:
            for cellid in res.cellids:
                irow = cellid[0]
                icol = cellid[1]
                k[ilay,irow,icol] = kn 
                
    elif type(layer) == int:
        for cellid in res.cellids:
            irow = cellid[0]
            icol = cellid[1]
            k[layer,irow,icol] = kn 
    
    else :
        raise Exception ("layer must be an int or a list of int")
        
#18
def liss_mob(arr,n,null_v = 0):
    
    """
    Apply a moving average (with 2*n numbers) on 2D array.
    arr : 2D numpy array
    n : number of elements (in one of the four direction) to take into account for the moving average (n=2 --> average of a specific number will be calculated with the surroundings 5x5 elements)
    return a 2D array and replace null value by 0
    """
    
    
    arr[arr==null_v]=None
    for irow in range(n,arr.shape[0]-n):
        for icol in range(n,arr.shape[1]-n):
            if not np.isnan(arr[irow,icol]):
                bloc = arr[irow-n:irow+n+1,icol-n:icol+n+1]
                arr[irow,icol] = np.nanmean(bloc)
    arr = np.nan_to_num(arr)
    return arr