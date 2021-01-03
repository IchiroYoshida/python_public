import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 緯度経度で範囲を指定する
north = 46.
south = 30.
east = 147.
#west = 128.
west = 128.

# 地図の表示('merc"は純粋に緯度経度を直行座標系にplotしている）
m = Basemap( projection='merc', llcrnrlat=south, urcrnrlat=north, llcrnrlon=west, urcrnrlon=east, resolution='l' )

# 陸地を茶色に, 湖を水色に
#m.fillcontinents(color='#8B4513', lake_color='#90FEFF')
#m.fillcontinents(color='coral', lake_color='aqua')

# 海を濃い青に
#m.drawlsmask(ocean_color='#00008b')
#m.drawlsmask(ocean_color='blue')
#m.drawmapboundary(fill_color='blue')

# NASA 'Blue marble' image
m.bluemarble()

# 海岸線を引く
m.drawcoastlines(linewidth=0.5, color='black')

# 5度ごとに緯度線を描く
m.drawparallels(np.arange(25, 50, 5), labels = [1, 0, 0, 0], fontsize=10)

# 5度ごとに経度線を描く
m.drawmeridians(np.arange(125, 150, 5), labels = [0, 0, 0, 1], fontsize=10)

# 画面に表示
plt.show()

