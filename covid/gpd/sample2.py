import matplotlib.pyplot as plt
import geopandas
import geoplot

world = geopandas.read_file(
        geopandas.datasets.get_path('naturalearth_lowres')
)
boroughs = geopandas.read_file(
        geoplot.datasets.get_path('nyc_boroughs')
)
collisions = geopandas.read_file(
        geoplot.datasets.get_path('nyc_injurious_collisions')
)

#geoplot.polyplot(world, figsize=(8, 4))

import mapclassify

gpd_per_person = world['gdp_md_est']/world['pop_est']

scheme = mapclassify.Quantiles(gpd_per_person, k=5)

geoplot.choropleth(
        world, hue=gpd_per_person, scheme=scheme,
        cmap='Greens', figsize=(8, 4)
)

plt.show()

