'''
Uranus position Nov.8 8:00 - 10:00 Moon eclipse.
'''
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import patches as patches

from skyfield.api import Star, load, N, E, wgs84
from skyfield.data import hipparcos #, mpc, stellarium
from skyfield.projections import build_stereographic_projection

# 初期時刻設定
ts = load.timescale()
t_observe = ts.utc(2022, 11, 8, 9, 0, range(0,3600*6, 600))
t = t_observe[len(t_observe) // 2]  # middle time

# An ephemeris from the JPL provides Earth, Moon and Uranus positions.
eph = load('de421.bsp')
earth, moon= eph['earth'], eph['moon']
uranus = eph['Uranus Barycenter']

#観測地点（福岡）
fukuoka = earth + wgs84.latlon(33.597 * N, 130.394 * E)
obs = fukuoka.at(t_observe)
cent = fukuoka.at(t)

#月の見かけの大きさ計算
moon_radius = 1737
moon_app = cent.observe(moon).apparent()
moon_ra, moon_dec, moon_distance = moon_app.radec()
moon_dist = moon_app.distance().km
moon_rad = np.arctan2(moon_radius, moon_dist)
#moon_deg = np.rad2deg(moon_rad)
print('moon_rad =',moon_rad)

# ヒッパルコス星表
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

# 天王星の位置
center = cent.observe(uranus).apparent()
projection = build_stereographic_projection(center)
field_of_view_degrees = 3.0
limiting_magnitude = 10.0

# プロットの図表(X,Y)
star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

uranus_x, uranus_y = projection(cent.observe(uranus))
moon_x,moon_y = projection(obs.observe(moon))

# 星の等級でのプロット
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]
marker_size = (0.5 + limiting_magnitude - magnitude) ** 2.0

# 星図のプロット
fig, ax = plt.subplots(figsize=[9, 9])

# 星のプロット 
ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
           s=marker_size, color='k')

# 月の位置と時刻
moon_color = '#f00'
offset = 0.0002

for xi, yi in zip(moon_x, moon_y):
   c = patches.Circle(xy=(xi, yi), radius=moon_rad, fc='y',ec ='k', zorder =0)
   ax.add_patch(c)
   
#ax.plot(moon_x, moon_y, 'x', c=moon_color, zorder=3)

for xi, yi, tstr in zip(moon_x, moon_y, t_observe.utc_strftime('%H:%M:%S')):
    tstr = tstr.lstrip('0')
    text = ax.text(xi , yi + offset, tstr, color=moon_color,
                   ha='left', va='top', fontsize=7, weight='bold', zorder=-1)
    text.set_alpha(0.5)


# 天王星の位置
uranus_color = '#00f'
offset = 0.0002

ax.plot(uranus_x, uranus_y, 'o', c=uranus_color, zorder=3)


# タイトル、パラメータの記入
angle = np.pi - field_of_view_degrees / 360.0 * np.pi
limit = np.sin(angle) / (1.0 - np.cos(angle))

print('limit =',limit )

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_aspect(1.0)
ax.set_title('Moon - Uranus positions {}'.format(
    t_observe[0].utc_strftime('%H:%M:%S'),
    t_observe[-1].utc_strftime('%H:%M:%S'),
))

# Save.

#fig.show()
fig.savefig('uranus-moon1.png', bbox_inches='tight')