import matplotlib.pyplot as plt
import geopandas as gpd

pop = pd.read_csv('worldPop.csv')
iso3 = pd.read_csv('wm_iso3.csv')
deathMil = pd.read_csv('DeathMil.csv',header=1)

merged1 = pd.merge(pop, iso3, how='outer',
        left_on='Country', right_on='Country')

merged2 = pd.merge(merged1, deathMil, how='outer',
        left_on='Country', right_on='Country')

world  = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#world = world[(world.pop_est>0) & (world.continent == "Africa")]

world.loc[world['name'] == 'France','iso_a3'] = 'FRA'
world.loc[world['name'] == 'Norway','iso_a3'] = 'NOR'
world.loc[world['name'] == 'Somaliland','iso_a3'] = 'SOM'
world.loc[world['name'] == 'Kosovo','iso_a3'] = 'RKS'

for_plotting = world.merge(merged2, left_on = 'iso_a3', right_on = 'iso3')

ax = for_plotting.dropna().plot(column='Deaths/Mil.',
        cmap = 'YlGnBu', figsize=(15,9),
        scheme='quantiles', k=3,
        legend = False,
        edgecolor = 'blue' );

fig = ax.get_figure()
cbax = fig.add_axes([0.95, 0.3, 0.03, 0.39])

sm = plt.cm.ScalarMappable(cmap = 'YlGnBu', \
    norm = plt.Normalize(vmin=0.0, vmax=40.0))

fig.colorbar(sm, cax=cbax, format="%d")

ax.set_title('Africa COVID-19 2020/6/10 Deaths/Mil. pop. ',fontdict={'fontsize':25})

ax.set_axis_off()

plt.show()
