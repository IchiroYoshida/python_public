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
t_observe = ts.utc(2022, 11, 8, 10, 0, range(0,3600*4, 600))
t = t_observe[len(t_observe) // 2]  # middle time

# An ephemeris from the JPL provides Earth, Moon and Uranus positions.
eph = load('de421.bsp')
earth, moon= eph['earth'], eph['moon']
uranus = eph['Uranus Barycenter']

#観測地点（福岡）
fukuoka = earth + wgs84.latlon(33.597 * N, 130.394 * E)
obs = fukuoka.at(t_observe)
cent = fukuoka.at(t)


# 観測時間の中央時刻を月の位置を中心に
center = cent.observe(moon).apparent()
projection = build_stereographic_projection(center)
field_of_view_degrees = 2.0
limiting_magnitude = 10.0

#月の見かけの大きさ計算
moon_radius = 1737
moon_app = obs.observe(moon).apparent()
moon_ra, moon_dec, moon_distance = moon_app.radec()
moon_dist = moon_app.distance().km
moon_rad = np.arctan2(moon_radius, moon_dist)

uranus_x, uranus_y = projection(obs.observe(uranus))
moon_x,moon_y = projection(obs.observe(moon))

xx = uranus_x - moon_x
yy = uranus_y - moon_y 

# 星図のプロット
fig, ax = plt.subplots(figsize=[9, 9])

# 天王星の相対位置プロット
uranus_color = '#00f'
offset = 0.0001

ax.plot(xx, yy, 'o', c=uranus_color, zorder = 0)

for xi, yi, tstr in zip(xx, yy, t_observe.utc_strftime('%H:%M')):
    tstr = tstr.lstrip('0')
    text = ax.text(xi , yi - offset, tstr, color=uranus_color,
                   ha='left', va='top', fontsize=7, weight='bold', zorder=0)
    text.set_alpha(0.5)

# 月のプロット
c = patches.Circle(xy=(0, 0), radius=moon_rad[0], fc='y', ec= 'k', zorder=-1)
ax.add_patch(c)

# タイトル、パラメータの記入
angle = np.pi - field_of_view_degrees / 360.0 * np.pi
limit = np.sin(angle) / (1.0 - np.cos(angle))

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_aspect(1.0)
ax.set_title('Moon - Uranus positions {}'.format(
    t_observe[0].utc_strftime('%Y-%m-%d %H:%M:%S'),
    t_observe[-1].utc_strftime('%H:%M:%S'),
))

# Save.

#fig.show()
fig.savefig('uranus-moon2.png', bbox_inches='tight')