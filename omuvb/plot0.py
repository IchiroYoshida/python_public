import h5py
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker

# Open the IMERG data file; it may be necessary to add a path if the file is not in the working directory.

data_file_path = '/Users/ichiro3/nasa/'

f = h5py.File(data_file_path+'OMI-Aura_L2-OMUVB_2020m0331t2328-o83570_v003-2020m0403t081359.he5','r')

# Read the EDD ,latitude, and longitude data:

EDD = f['HDFEOS/SWATHS/UVB/Data Fields/Irradiance380'][0][:]
EDD = np.ravel(EDD)
MaxEDD =np.max(EDD)

print('EDD',EDD,MaxEDD)

theLats = f['HDFEOS/SWATHS/UVB/Geolocation Fields/Latitude'][:]
theLats = np.ravel(theLats)
theLons = f['HDFEOS/SWATHS/UVB/Geolocation Fields/Longitude'][:]
theLons = np.ravel(theLons)

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

cmap = plt.get_cmap('coolwarm')
plt.scatter(theLons, theLats, c=cmap(EDD))
plt.title('OMI-Aura_Level2 OMUVB Apr.2020', size=24)
plt.colorbar()

# Save the figure as a PNG:

fig.savefig('OMUVBI380_plot.png', bbox_inches='tight', pad_inches = 0.1)
'''

