import os
import h5py
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker

data_file_path = './nasa/Level3/'
data_file_out_path = './nasa/out/'

Val0 = np.zeros((180, 360), dtype=float)
Val1 = np.zeros((180, 360), dtype=float)
Tmp0 = np.zeros((180*360), dtype=float)
Tmp1 = np.zeros((180*360), dtype=float)

NUM = int(180*360)

def drawCcrs(Val,fname):
    Lon = np.linspace(-180,180,360)
    Lat = np.linspace(-90,90,180)
    x, y = np.meshgrid(Lon, Lat)

    # Set the figure size, projection, and extent
    fig = plt.figure(figsize=(21,7))
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0))
    ax.set_extent([-180,180,-90,90], ccrs.PlateCarree())  

    # Add coastlines and formatted gridlines
    ax.coastlines(resolution="110m",linewidth=1)
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', linestyle='--')
    gl.xlines = True
    gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])
    gl.ylocator = mticker.FixedLocator([-60, -50, -25, 0, 25, 50, 60])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size':16, 'color':'black'}
    gl.ylabel_style = {'size':16, 'color':'black'}

    # Set contour levels and draw the plot.
    clevs = np.arange(0,9000, 100)

    plt.contourf(x, y, Val, clevs, cmap=plt.cm.rainbow)
    plt.title('OMI-Aura_Level3 OMUVBd May.1,2020', size=24)
    plt.colorbar()

    # Save the figure as a PNG:

    file_name = data_file_out_path+(fname+'.png')
    fig.savefig(file_name, bbox_inches='tight', pad_inches = 0.1)
 
# Plot the data using matplotlib and cartopy

files = os.listdir(data_file_path)
files.sort()

file = files[0]
fname =file.split('_v003')[0]
print('No.1:',fname) 

f = h5py.File(data_file_path+file,'r')
Tmp0 = np.array(f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/ErythemalDailyDose'][:][:].flatten())

file = files[1]
fname = file.split('_v003')[0]
print('No.2:',fname)

f = h5py.File(data_file_path+file,'r')
Tmp1 = np.array(f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/ErythemalDailyDose'][:][:].flatten())

for i in range(NUM):
    val0 = Tmp0[i]
    val1 = Tmp1[i]
    if (val0 < 0):
        if(val1 > 0):
            Tmp1[i] = val1
    else:
        if(val1 > 0):
            Tmp1[i] = (val0 + val1)/2.
        else:
            Tmp1[i] = val0

#Tmp0 = Tmp1

Val0=np.reshape(Tmp0,(180,360))
Val1=np.reshape(Tmp1,(180,360))

drawCcrs(Val0,'Val0')
drawCcrs(Val1,'Val1')

