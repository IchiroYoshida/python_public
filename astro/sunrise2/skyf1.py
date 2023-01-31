# Sun rise 2023-01-01  
# Inverse of the sunrise equation - finding locations with a given sunrise time on a given day.

#from datetime import datetime
#import ephem
from skyfield.api import Topos, load
from pytz import timezone
import numpy as np
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import scipy.optimize as spo

ts = load.timescale()
t = ts.utc(2023, 1, 1, 6, 47, 49)
tz = timezone('Asia/Tokyo')

eph = load('de421.bsp')
sun, earth = eph['sun'], eph['earth']

def sun_alt(lon, lat, t):
    position = earth + Topos(str(lon)+' N',str(lat)+' E')
    sun_alt = position.at(t).observe(sun).apparent().altaz()[0].degrees
    return (sun_alt)

lats = np.linspace(20, 46 , 27)

longis = []
lons = []
lon0 = 135.

for lat in lats:
       answer, info = spo.brentq(sun_alt, lon0-90, lon0+90,
                                 args=(lat, t),
                                 full_output = True )
       if info.converged:
           lons.append(answer)
       else:
           lons.append(None)
       lons = [(lon+180)%360.-180 for lon in lons] # wraparound at +/1 180
       longis.append(lons)

print(lons)
'''
# 描画サイズ指定
fig = plt.figure(figsize=(10, 10), facecolor="white",tight_layout=True)
ax = fig.add_subplot(111, projection=ccrs.Mercator(central_longitude=140.0), facecolor="white")
ax.set_global()
ax.coastlines()

# ラベル表示
ax.gridlines(draw_labels=True)

# 描画位置（Lon, Lat）指定
ax.set_extent([120.0, 150.0, 20.0, 50.0], crs=ccrs.PlateCarree())
gl = ax.gridlines(draw_labels=True)
gl.xlocator = mticker.FixedLocator(np.arange(120, 150.1, 1.0))
gl.ylocator = mticker.FixedLocator(np.arange(20, 50.1, 1.0))
ax.plot(lons,lats, transform=ccrs.PlateCarree())
plt.title('日本', fontsize=15)

plt.show()
'''
