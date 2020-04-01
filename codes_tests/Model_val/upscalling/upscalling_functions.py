import numpy  as np
import pandas as pd
import pickle
import matplotlib.pyplot  as plt

##############
##############

def read_pickle(path):
    '''
    Function to read a pickle file.
    '''
    
    with open(path, 'rb')as file:
        f_read = pickle.load(file)
    
    return f_read


##############
##############

def write_pickle(path, data):
    '''
    Function to write a picke file.
    '''
    
    with open(path,'wb')as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        

##############
##############

def assign_k(simu, facies_list, k_list):
    '''
    Function to assign permeability values to categ simulation.
    
    -------
    Input : 
    simu = np array from the simulation (ny,nx).
    facies_list = list of the categ facies number [0,1,2..].
    k_list = list of the permeability values for each facies [1e-2,1e-4...].
    
    -------
    Output:
    simu_k : np array (ny,nx) with the permeability values assigned.
    '''
    
    simu_k = np.copy(simu)
    
    for f,k in zip(facies_list, k_list):
        
        krd = np.random.random(simu_k.shape)*k
        simu_k[simu_k==f] = krd[simu_k==f]
    
    return simu_k


##############
##############

def create_mask(grid):
    '''
    Create a mask from a define grid numpy (ny,nx).
    
    --------
    Input :
    grid = np array
    
    --------
    Output : 
    mask = a binary numpy array: 0 outside, 1 inside.
    '''
    mask = np.ones(grid.shape)
    mask[np.isnan(grid)] = 0
    
    return mask


##############
##############


def up_array_mean(arr, sx, sy, sx_up, sy_up):
    '''
    Function to upscall a np array (ny,nx) to a defined output resolution.
    
    -------
    Input:
    arr = np array to upscal.
    sx, sy = Dimension of the cells of the input grid.
    sx_up, sy_up = Dimension of the output upscalled cells.
    
    -------
    Output:
    means : array (ny,nx), upscalled grid with simple means.
    '''
    
    #Define dimension and spacing.
    nx, ny       = arr.shape[1], arr.shape[0]
    nx_up, ny_up = nx*sx/sx_up, ny*sy/sy_up
    sx_up, sy_up = sx_up, sy_up
    
    values = np.copy(arr) #[ny,nx]
    
    #Add empty lines/columns while the extend of the upscalled grid does not match the extend of the original grid. 
    while nx_up/int(nx_up)!= 1.0:
        add_h  = np.full((values.shape[0],1), np.nan)
        values = np.hstack((values,add_h))
        nx     = values.shape[1]
        nx_up  = nx*sx/sx_up

    while ny_up/int(ny_up)!= 1.0:
        add_v  = np.full((1,values.shape[1]), np.nan) 
        values = np.vstack((values,add_v)) 
        ny     = values.shape[0]
        ny_up  = ny*sy/sy_up
    
    #Coordinnates of the original grid cells.
    coord_x = np.arange(sx/2,nx*sx+sx/2,sx)
    coord_y = np.arange(sy/2,ny*sy+sy/2,sy)
    coords  = np.array([[co_x, co_y] for co_y in coord_y for co_x in coord_x])
    
    #For each cells or the original grid we assign its novel p/cell position in the upscalled grid (flattend position)
    p_x = [int(np.trunc(cx/sx_up)) for cx in coords[:,0]]
    p_y = [int(np.trunc((cy/sy_up))*nx) for cy in coords[:,1]]
    p = np.array([[px+py] for px,py in zip(p_x,p_y)])
    
    #Group the cells id by new position
    groups = {}
    for i,pos in enumerate(p):
        if pos[0] in groups.keys():
            groups[pos[0]].append(i)
        else:
            groups[pos[0]] = []
            groups[pos[0]].append(i)

    #Calculate the mean value of every groups.
    means = mean_array(groups, values, nx_up, ny_up)    
    print('The shape of the ouptut grid is {}'.format(means.shape))
    print('The original cells dimensions were sx = {} and sy = {}.'.format(sx,sy))
    print('The upscall cells dimensions are sx_up = {} and sy_up = {}.'.format(sx_up,sy_up))
    print('Upscalling is done!')
    
    return means


##############
##############

def mean_array(groups, values, nx_up, ny_up):
    '''
    To perform a simple mean operation during upscalling.
    Used within the up_array_mean() function.
    '''
    
    means = np.full((int(nx_up*ny_up)),np.nan)
    
    for i, key in enumerate(groups.keys()):
        val_group = [values.flatten()[cell] for cell in groups[key]]
        means[i]  = (np.nanmean(val_group))
        
    return np.reshape(means,(int(ny_up),int(nx_up)))


##############
##############

def up_flopy_mean(arr, sx, sy,  grid_up):
    '''
    Function to upscall a np array (ny,nx) to a Flopy grid. 
    The output grid may be structured or un-structured.
    
    -------
    Input:
    arr = np array to upscal.
    sx, sy  = Dimension of the cells of the input grid.
    grid_up = Flopy grid create with GridGen.
    
    -------
    Output:
    means = np array (len(nbCell grid_up)),  upscalled grid with simple means.
    '''
    
    #Define dimension and spacing.
    nx, ny = arr.shape[1], arr.shape[0]
    sx, sy = sx, sy
    nx_up, ny_up = grid_up.dis.ncol.get_data(), grid_up.dis.nrow.get_data()
    sx_up, sy_up = grid_up.dis.delc[0], grid_up.dis.delr[0]
    
    values = np.copy(arr) #[ny,nx]
    
    #Add empty lines/columns while the extend of the upscalled grid does not match the extend of the original grid. 
    while nx_up/int(nx_up)!= 1.0:
        add_h  = np.full((values.shape[0],1), np.nan) 
        values = np.hstack((values,add_h))
        nx     = values.shape[1]
        nx_up  = nx*sx/sx_up

    while ny_up/int(ny_up)!= 1.0:
        add_v  = np.full((1,values.shape[1]), np.nan) 
        values = np.vstack((values,add_v)) 
        ny     = values.shape[0]
        ny_up  = ny*sy/sy_up

    #Properties of the flopy grid and its cells.
    gridprops = grid.get_gridprops_disv() 
    vertices  = gridprops['vertices'] 
    cell2d    = gridprops['cell2d']
    
    #Coordinnates of the original grid cells.
    coord_x = np.arange(sx/2,nx*sx+sx/2,sx)
    coord_y = np.arange(sy/2,ny*sy+sy/2,sy)
    
    #Bounds list of the new upscalled grid.
    cells_bounds = []
    for i in range(len(cell2d)):
        x_min = vertices[cell2d[i][4]][1]
        x_max = 0

        for ind in cell2d[i][5:-1]:
            x_m = vertices[ind][1]
            if x_m> x_max:
                x_max = x_m

        y_max = vertices[cell2d[i][4]][2]
        y_min = y_max 

        for ind in cell2d[i][5:-1]:
            y_m = vertices[ind][2]
            if y_m<y_min:
                y_min = y_m

        cells_bounds.append(np.array([[x_min, x_max, x_max-x_min],[y_min, y_max, y_max-y_min]]))
        
    cells_bounds = np.array(cells_bounds)

    #Group each cell to its upscalled cell in regard of the bounds values and the coordinnates.
    groups={}
    idCell=0
    for j in range(ny):
        for i in range(nx):
            coord = [coord_x[i], coord_y[j]]
            value = values[j,i]
            for ind, bound in enumerate(cells_bounds):######IND not i WARNING not clean but work
                if coord[0]> bound[0][0] and coord[0]<= bound[0][1] and coord[1]> bound[1][0] and coord[1]<= bound[1][1]:
                    if ind in groups.keys():
                        groups[ind].append(value)
                        
                    else:
                        groups[ind]=[]
                        groups[ind].append(value)
                    idCell+=1
                    break
    
    #Calculate the mean value of every groups.
    means = mean_flopy(groups)    
    print('The original cells dimension were sx = {} and sy = {}.'.format(sx, sy))
    print('The upscall cells dimension are sx_up = {} and sy_up = {}.'.format(sx_up,sy_up))
    print('Upscalling is done!')
    
    return means


##############
##############

def mean_flopy(groups):
    '''
    To perform a simple mean operation during upscalling.
    Used within the up_flopy_mean and up_flopy functions.
    '''

    means = np.array([np.nanmean(groups[k]) for k in np.sort(list(groups.keys()))])
    return means


##############
##############

def up_flopy_kb(arr, sx, sy, grid_up):
    '''
    Function to upscall a np array (ny,nx) to a Flopy grid. 
    The output grid may be structured or un-structured.
    
    -------
    Input:
    arr = np array to upscal.
    sx, sy  = Dimension of the cells of the input grid.
    grid_up = Flopy grid create with GridGen.
    
    -------
    Output:
    kmax_X = np array (len(nbCell grid_up)),  upscalled iteratively starting from arithmetic means along the x axis. 
    kmin_X = np array (len(nbCell grid_up)),  upscalled iteratively starting from harmonic means along the x axis.
    
    kmax_Y = np array (len(nbCell grid_up)),  upscalled iteratively starting from arithmetic means along the y axis. 
    kmin_Y = np array (len(nbCell grid_up)),  upscalled iteratively starting from harmonic means along the y axis.
    '''    
    
   #Define dimension and spacing.
    nx, ny = arr.shape[1], arr.shape[0]
    sx, sy = sx, sy
    nx_up, ny_up = grid_up.dis.ncol.get_data(), grid_up.dis.nrow.get_data()
    sx_up, sy_up = grid_up.dis.delc[0], grid_up.dis.delr[0]

    values = np.copy(arr) #[ny,nx]
    
    #Add empty lines/columns while the extend of the upscalled grid does not match the extend of the original grid. 
    while nx_up/int(nx_up)!= 1.0:
        add_h  = np.full((values.shape[0],1), np.nan) 
        values = np.hstack((values,add_h))
        nx     = values.shape[1]
        nx_up  = nx*sx/sx_up

    while ny_up/int(ny_up)!= 1.0:
        add_v  = np.full((1,values.shape[1]), np.nan) 
        values = np.vstack((values,add_v)) 
        ny     = values.shape[0]
        ny_up  = ny*sy/sy_up
        
        #Properties of the flopy grid and its cells.
    gridprops = grid_up.get_gridprops_disv() 
    vertices  = gridprops['vertices'] 
    cell2d    = gridprops['cell2d']
    
    #Coordinnates of the original grid cells.
    coord_x = np.arange(sx/2,nx*sx+sx/2,sx)
    coord_y = np.arange(sy/2,ny*sy+sy/2,sy)
    

    #Bounds list of the new upscalled grid.
    cells_bounds = []
    for i in range(len(cell2d)):
        x_min = vertices[cell2d[i][4]][1]
        x_max = 0

        for ind in cell2d[i][5:-1]:
            x_m = vertices[ind][1]
            if x_m> x_max:
                x_max = x_m

        y_max = vertices[cell2d[i][4]][2]
        y_min = y_max 

        for ind in cell2d[i][5:-1]:
            y_m = vertices[ind][2]
            if y_m<y_min:
                y_min = y_m

        cells_bounds.append(np.array([[x_min, x_max, x_max-x_min],[y_min, y_max, y_max-y_min]]))
        
    cells_bounds=np.array(cells_bounds)
    
    #Group each cell to its upscalled cell in regard of the bounds values and the coordinnates.
    groups_values = {}
    groups_id     = {} 
    for j in range(ny):
        for i in range(nx):
            coord = [coord_x[i], coord_y[j]]
            value = values[j,i]
            
            for ind, bound in enumerate(cells_bounds):
                if coord[0]> bound[0][0] and coord[0]<= bound[0][1] and coord[1]> bound[1][0] and coord[1]<= bound[1][1]:
                    
                    if ind in groups_values.keys():
                        groups_values[ind].append(value)
                        groups_id[ind].append(coord)
                        
                    else:
                        groups_values[ind] = []
                        groups_id[ind]     = []
                        groups_values[ind].append(value)
                        groups_id[ind].append(coord)
                    break
                    
    #Compute kmin and kmax
    kmax_x = []
    kmin_x = []
    for k in np.sort(list(groups_values.keys())):
            v_sub     = sub_matrix(groups_id[k], groups_values[k], sx, sy)
            kX, error = kx(v_sub)
            
            if error   == 0:            
                kmax_x.append(kX[0][0,0])
                kmin_x.append(kX[1][0,0])
                
            elif error == 1:
                kmax_x.append(np.nan)
                kmin_x.append(np.nan)
    
    if len(cell2d)!=len(kmax_x) or len(cell2d)!=len(kmin_x):
        print('Issue! K is not the same length as nb(cell2d)!')
        print
 

    kmax_x = np.array(kmax_x)
    kmin_x = np.array(kmin_x)
    print('The original cells dimension were sx = {} and sy = {}.'.format(sx, sy))
    print('The upscall cells dimension are sx_up = {} and sy_up = {}.'.format(sx_up,sy_up))
    print('Upscalling is done!')
    
    return kmax_x, kmin_x


##############
##############

def sub_matrix(coord_gpr, val_gpr, sx, sy):
    '''
    Create the matrix for the conductivity upscalling calculation.
    Used in up_flopy_kb function.
    '''
    x = [g[0] for g in coord_gpr]
    y = [g[1] for g in coord_gpr]
    
    x0, y0 = min(x), min(y)
    sx, sy = sx, sy
    
    j = ((y - y0) / sy).astype(int)
    i = ((x - x0) / sx).astype(int)
    
    nx, ny = max(i), max(j)
    value = np.full((ny+1,nx+1),np.nan)
    value[j,i] = val_gpr
    
    return value   


##############
##############
    
def kx(grid):
    '''
    Compute kx max and min from an input grid (np array).
    Used in up_flopy_kb function.
    '''
    
    #If the grid is only composed of nan values we skip the calculation.
    nb_nan = np.count_nonzero(np.isnan(grid))
    
    if nb_nan == (grid.shape[0]*grid.shape[1]):
        kmax = np.nan
        kmin = np.nan
        err  = 1
    else:
        kmax = kmax_x(grid)
        kmin = kmin_x(grid)
        err  = 0
       
    return [kmax, kmin,], err


##############
##############

def kmax_x(grid):
    '''
    Compute the kmax value along x, by simple iterative artihmetic/harmonic means.
    Used in kx function.
    '''
        
    val = np.copy(grid)
    while val.shape != (1,1):

        #arithmetic mean
        mean_a = []
        nt = int(np.trunc(val.shape[0]/2))
        if nt >0 :
            for t in range(nt):
                l1 = val[t*2]
                l2 = val[(t*2+1)]
                mean_a.append(np.nanmean([l1,l2], axis=0))

            val = val[(t*2)+2:]
            for m in mean_a[::-1]:
                val = np.vstack([m,val])

        #harmonic mean
        mean_h = []
        nt = int(np.trunc(val.shape[1]/2))
        if nt>0:
            for t in range(nt):
                c1 = val[:,t*2]
                c2 = val[:,t*2+1]

                if np.count_nonzero(~np.isnan([c1,c2])) != len(c1)+len(c2):
                    mh=[]
                    for c in range(len(c1)):
                        nb = np.count_nonzero(~np.isnan([c1[c],c2[c]]))
                        mh.append(nb/np.nansum([1/c1[c],1/c2[c]])) 
                    mh = np.array(mh)
                    mean_h.append(mh)

                else:
                    mean_h.append(2/ np.nansum([1/c1,1/c2], axis=0))

            val = val[:,t*2+2:]
            for m in mean_h[::-1]:
                val = np.hstack([m.reshape(len(m),1),val])

    return val

    
##############
##############
    
def kmin_x(grid):
    '''
    Compute the kmin value along x, by simple iterative harmonic/arithme means.
    Used in kx function.
    '''
    val = np.copy(grid)
    while val.shape != (1,1):

        #harmonic mean
        mean_h = []
        nt = int(np.trunc(val.shape[1]/2))
        if nt>0:
            for t in range(nt):
                c1 = val[:,t*2]
                c2 = val[:,t*2+1]

                if np.count_nonzero(~np.isnan([c1,c2])) != len(c1)+len(c2):
                    mh=[]
                    for c in range(len(c1)):
                        nb = np.count_nonzero(~np.isnan([c1[c],c2[c]]))
                        mh.append(nb/np.nansum([1/c1[c],1/c2[c]])) 
                    mh = np.array(mh)
                    mean_h.append(mh)

                else:
                    mean_h.append(2/ np.nansum([1/c1,1/c2], axis=0))

            val = val[:,t*2+2:]
            for m in mean_h[::-1]:
                val = np.hstack([m.reshape(len(m),1),val])

        #arithmetic mean
        mean_a = []
        nt = int(np.trunc(val.shape[0]/2))
        if nt >0 :
            for t in range(nt):
                l1 = val[t*2]
                l2 = val[(t*2+1)]
                mean_a.append(np.nanmean([l1,l2], axis=0))

            val = val[(t*2)+2:]
            for m in mean_a[::-1]:
                val = np.vstack([m,val])

    return val

    
##############
##############

#To do the same for y direction
