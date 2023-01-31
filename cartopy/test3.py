
import numpy as np
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt

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
plt.title('日本', fontsize=15)

plt.show()
