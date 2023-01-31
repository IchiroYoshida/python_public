import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
#ax.coastlines()
ax.stock_img()

plt.show()

