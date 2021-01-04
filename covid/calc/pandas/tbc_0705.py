import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable

WB_CSV = 'WB_TBC.csv'
YR = '2018'

tbc = pd.read_csv(WB_CSV,header=4, usecols=['Country Code',YR])
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#world = world[(world.pop_est>0) & (world.continent == "Asia")]
 
world.loc[world['name'] == 'France','iso_a3'] = 'FRA'
world.loc[world['name'] == 'Norway','iso_a3'] = 'NOR'
world.loc[world['name'] == 'Somaliland','iso_a3'] = 'SOM'
world.loc[world['name'] == 'Kosovo','iso_a3'] = 'RKS'

for_plotting = world.merge(tbc, left_on = 'iso_a3', right_on = 'Country Code')

fig, ax = plt.subplots(1, 1)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

for_plotting.dropna().plot(column=YR,
        cmap = 'YlGnBu', figsize=(15, 9),
        edgecolor='blue', ax=ax, legend=True, cax=cax)

Title = ('Incidence of tuberculosis (per 100,000 people) %s'%(YR))
ax.set_title(Title, fontdict={'fontsize':25})
#ax.set_axis_off()
plt.show()
