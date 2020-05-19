import h5py
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker

data_file_path = '/Users/ichiro3/nasa/Level3/'

f = h5py.File(data_file_path+'OMI-Aura_L3-OMUVBd_2020m0501_v003-2020m0505t093001.he5','r')

# Read the Value

Val =f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/Irradiance380'][:][:]

Val0 = np.ravel(Val)
Max = np.max(Val0)
Min = np.min(Val0)
Ave = np.mean(Val0)

print('Max = %f Ave = %f Min = %f'%(Max,Ave,Min))

Lon = np.linspace(-180,180,360)
Lat = np.linspace(-90,90,180)
x, y = np.meshgrid(Lon, Lat)

# Plot the data using matplotlib and cartopy

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
clevs = np.arange(0, 1000, 50)
plt.contourf(x, y, Val, clevs, cmap=plt.cm.rainbow)
#plt.scatter(x, y, c=cmap(Val))
plt.title('OMI-Aura_Level3 OMUVBd May.1,2020', size=24)
plt.colorbar()

# Save the figure as a PNG:

fig.savefig('OMUVBdIR380.png', bbox_inches='tight', pad_inches = 0.1)

