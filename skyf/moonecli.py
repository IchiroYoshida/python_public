from skyfield.api import load
from pytz import timezone
import numpy as np

# 初期時刻設定
ts = load.timescale()
t = ts.utc(2022, 11, 8, 9, 0, range(0, 15000))
tz = timezone('Asia/Tokyo')

# 太陽・月・地球
eph = load('de421.bsp')
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# 太陽・月の位置計算
sun_app = earth.at(t).observe(sun).apparent()
moon_app = earth.at(t).observe(moon).apparent()

# 太陽・月の見かけの大きさ計算
r_sun = 696000
sun_dist = sun_app.distance().km
sun_rad = np.arctan2(r_sun, sun_dist)

r_moon = 1737
moon_dist = moon_app.distance().km
moon_rad = np.arctan2(r_moon, moon_dist)

# 視差・本影の視半径計算
r_earth = 6378
parallax_sun = r_earth / sun_dist
parallax_moon = r_earth / moon_dist
umbra = (parallax_moon - sun_rad + parallax_sun) * 51/50

# 月・地球の本影の角距離の計算
app_sep = abs(sun_app.separation_from(moon_app).radians - np.deg2rad(180))

# 食分の計算
percent_eclipse = (umbra + moon_rad - app_sep) / (moon_rad * 2)
    
# 食の最大の検索	
max_i = np.argmax(percent_eclipse)
    
print('食の最大:', t[max_i].astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')
print('最大食分: {0:.2f}'.format(percent_eclipse[max_i]))

# 欠け始めと食の終わりの検索
eclipse = False

for ti, pi in zip(t, percent_eclipse):
    if pi > 0 :
        if eclipse == False:
            print('欠け始め:', ti.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')
            eclipse = True
    else :
        if eclipse == True:
            print('食の終わり:', ti.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')
            eclipse = False