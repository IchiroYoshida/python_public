#http://cyclodextrin.hatenablog.com/entry/2017/09/15/013738
# coding: utf-8

# 必要なモジュールのインポート
import numpy as np
import ephem
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from datetime import datetime as dt
from datetime import timedelta as td

# 人工衛星の軌道要素を入力（書き下し形式）
object_name = "Michibiki"       # 衛星名
epoch_date = "17235.85543054"   # 以下の軌道要素が観測された時刻
inclination = 40.8777           # 軌道平面の傾き（度）
RAofAN = 158.3480               # 昇交点の赤経（度, 春分点基準）
eccentricity = 0.0754024        # 軌道の離心率 (必ず1未満)  　　
arg_perigee = 270.5910          # 近点引数（度）
mean_anomaly = 347.7789         # 平均近点角(度)
mean_motion = 1.00258630        # 平均回転数（周回/日)
decay_rate = 0.00000228         # 軌道減衰率（周回/日^2)
orbit_num = 2543                # これまでの積算周回数

# epoch_dateをXEphem用の形式に変換
year = int(epoch_date[:2])
if (year >= 57):
    year += 1900
else:
    year += 2000
dayno = float(epoch_date[2:])
epoch_date_sl = "1/%s/%s" % (dayno, year)

# epoch_dateから一分ごとの時刻を3600個作成
decimal_time = dt(year, 1, 1) + td(dayno - 1)
time_list = [(decimal_time + td(hours=i/60)).strftime("%Y/%m/%d %H:%M:%S") for i in range(0,3600)]

# 世界地図を描写
m = Basemap()
m.drawcoastlines()

# 一分ごとの人工衛星の位置をプロット
for item in time_list:
    orbit_data = ",".join(map(str, (object_name, "E", epoch_date_sl, inclination, RAofAN, eccentricity, arg_perigee, mean_anomaly, mean_motion, decay_rate, orbit_num)))
    satellite = ephem.readdb(orbit_data)
    satellite.compute('%s' % item)
    latitude = satellite.sublat / ephem.degree
    longitude = satellite.sublong / ephem.degree
    x1,y1 = m(longitude, latitude)
    m.plot(x1, y1, "m.", markersize=1)

# プロット表示
plt.show()

