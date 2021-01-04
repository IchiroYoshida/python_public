import geopandas
import matplotlib.pyplot as plt

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
cities = geopandas.read_file(
	geopandas.datasets.get_path('naturalearth_cities'))

print(world.keys())
print(cities.keys())

city2 = cities['name']
geo2 = cities['geometry']

for city in range(len(city2)):
    print(city2[city],geo2[city])

#world.plot()
#plt.show()

