import matplotlib.pyplot as plt
import geopandas

world = geopandas.datasets.get_path('naturalearth_lowres')
cities = geopandas.datasets.get_path('naturalearth_cities')


df_world = geopandas.read_file(world)
df_cities = geopandas.read_file(cities)

pos = df_cities['geometry']
print(pos)


#base = df_world.plot(color='white', edgecolor='black')
#df_cities.plot(ax=base, marker='o', color='red', markersize=5);

#plt.show()

