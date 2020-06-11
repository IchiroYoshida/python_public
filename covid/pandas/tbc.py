import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

WB_CSV = 'WB_TBC.csv'
YR = '2018'

tbc = pd.read_csv(WB_CSV,header=4, usecols=['Country Code',YR])
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.continent == "Asia")]
 
world.loc[world['name'] == 'France','iso_a3'] = 'FRA'
world.loc[world['name'] == 'Norway','iso_a3'] = 'NOR'
world.loc[world['name'] == 'Somaliland','iso_a3'] = 'SOM'
world.loc[world['name'] == 'Kosovo','iso_a3'] = 'RKS'

for_plotting = world.merge(tbc, left_on = 'iso_a3', right_on = 'Country Code')

ax = for_plotting.dropna().plot(column=YR,
        cmap = 'YlGnBu',figsize=(12,9),legend=False, edgecolor='blue')


fig = ax.get_figure()
cbax = fig.add_axes([0.95, 0.3, 0.03, 0.39])

sm = plt.cm.ScalarMappable(cmap='YlGnBu',\
        norm = plt.Normalize(vmin=min(tbc[YR]), vmax=max(tbc[YR])))

fig.colorbar(sm, cax=cbax, format="%d")

Title = ('Incidence of tuberculosis (per 100,000 people) %s'%(YR))

ax.set_title(Title, fontdict={'fontsize':25})

ax.set_axis_off()

plt.show()
