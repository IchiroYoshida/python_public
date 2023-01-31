
import cartopy.crs as ccrs
import cartopy.feature as cfea
import matplotlib.pyplot as plt

# 描画サイズ指定
plt.figure(figsize=(10, 10))
ax = plt.axes(projection=ccrs.PlateCarree())

# ラベル表示
ax.gridlines(draw_labels=True)

# 描画位置（Lon, Lat）指定
ax.set_extent((120.0, 150.0, 20.0, 50.0), ccrs.PlateCarree())

# 海洋と陸地の色を指定
ax.add_feature(cfea.OCEAN,color='#00FFFF')
ax.add_feature(cfea.LAND,color='#32CD32')

plt.title('japan', fontsize=15)

# 画像保存
#plt.savefig('cartopy.png')
plt.show()
