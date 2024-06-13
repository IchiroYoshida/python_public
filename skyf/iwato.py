'''
天岩戸日食の計算
247.03.24 or 248.09.05

'''
from skyfield.api import load, wgs84
from datetime import timedelta
from pytz import timezone
import numpy as np

# 時刻設定
ts = load.timescale()
t = ts.utc(522, 6, 10, 0, 0, range(0,12000))
tz = timezone('Asia/Tokyo')

# 天体暦設定 -3000 to 3000 de422.bsp
eph = load('de422.bsp')
#eph = load('de421.bsp')

sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# 観測地設定
#fukuoka = wgs84.latlon(33.5930, 130.3903)
#umi = wgs84.latlon(33.55923, 130.54263)
#pos = earth+wgs84.latlon(33.3236, 130.3836) #吉野ヶ里
pos = earth+wgs84.latlon(34.5393, 135.8411) #纏向遺跡

# 太陽・月の位置計算
sun_app = pos.at(t).observe(sun).apparent()
moon_app = pos.at(t).observe(moon).apparent()

# 太陽・月の見かけの大きさ計算
r_sun = 696000
sun_dist = sun_app.distance().km
sun_rad = np.arctan2(r_sun, sun_dist)

r_moon = 1737
moon_dist = moon_app.distance().km
moon_rad = np.arctan2(r_moon, moon_dist)

# 太陽・月の角距離の計算
app_sep = sun_app.separation_from(moon_app).radians

# 食分の計算
percent_eclipse = (sun_rad + moon_rad - app_sep) / (sun_rad * 2)
    
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