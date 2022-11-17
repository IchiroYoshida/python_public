'''
Uranus position Nov.1 -15
'''
import math
import numpy as np
from pytz import timezone

from matplotlib import pyplot as plt
from matplotlib import patches as patches
from matplotlib.collections import LineCollection

from skyfield.api import Star, load, N, E, wgs84
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN
from skyfield.data import hipparcos, mpc, stellarium
from skyfield.projections import build_stereographic_projection

# 初期時刻設定

ts = load.timescale()
t_uranus = ts.utc(2022, 11, range(1, 15, 3))
t = t_uranus[len(t_uranus) // 2]  # middle date

# An ephemeris from the JPL provides Sun, Earth, Moon and Uranus positions.

eph = load('de421.bsp')
sun, earth, moon= eph['sun'], eph['earth'], eph['moon']
uranus = eph['Uranus Barycenter']

#観測地点（福岡）
fukuoka = earth + wgs84.latlon(33.597 * N, 130.394 * E)
f = fukuoka.at(t)

# 太陽、月、天王星の地球からの視位置計算（月間中央値）
sun_app = f.observe(sun).apparent()
moon_app = f.observe(moon).apparent()
uranus_app = f.observe(uranus).apparent()

# ヒッパルコス星表
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

# 天王星の観測期間での中心位置
center = earth.at(t).observe(uranus)
projection = build_stereographic_projection(center)
field_of_view_degrees = 3.0
limiting_magnitude = 8.0

# プロットの図表(X,Y)
star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

uranus_x, uranus_y = projection(earth.at(t_uranus).observe(uranus))

# 星の等級でのプロット
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]
marker_size = (0.5 + limiting_magnitude - magnitude) ** 2.0

# 星図のプロット
fig, ax = plt.subplots(figsize=[9, 9])

# 星のプロット 
ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
           s=marker_size, color='k')

# 天王星の位置と日付
uranus_color = '#00f'
offset = 0.0002

ax.plot(uranus_x, uranus_y, '+', c=uranus_color, zorder=3)

for xi, yi, tstr in zip(uranus_x, uranus_y, t_uranus.utc_strftime('%m/%d')):
    tstr = tstr.lstrip('0')
    text = ax.text(xi , yi - offset, tstr, color=uranus_color,
                   ha='left', va='top', fontsize=7, weight='bold', zorder=-1)
    text.set_alpha(0.5)

# タイトル、パラメータの記入
angle = np.pi - field_of_view_degrees / 360.0 * np.pi
limit = np.sin(angle) / (1.0 - np.cos(angle))

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_aspect(1.0)
ax.set_title('Uranus positions {}'.format(
    t_uranus[0].utc_strftime('%Y %B %d'),
    t_uranus[-1].utc_strftime('%Y %B %d'),
))

# Save.

#fig.show()
fig.savefig('uranus-chart.png', bbox_inches='tight')