from skyfield.api import Topos, load
from datetime import timedelta
from pytz import timezone

# 時刻設定
ts = load.timescale()
t0 = ts.now()
t1 = ts.utc(t0.utc_datetime() + timedelta(days=10))
tz = timezone('Asia/Tokyo')

# 天体暦設定
eph = load('de421.bsp')
sun, earth = eph['sun'], eph['earth']

# 観測地設定
fukuoka = Topos('33.5930 N', '130.3903 E')

# 国際宇宙ステーションの軌道要素設定
satellites = load.tle('http://celestrak.com/NORAD/elements/stations.txt')
iss = satellites['ISS (ZARYA)']

# 指定時刻間に福岡上空を通るパスの検索
t, events = iss.find_events(fukuoka, t0, t1, altitude_degrees=10.0)

# 太陽高度、および太陽光が当たっているかの計算
sun_alt = (earth + fukuoka).at(t).observe(sun).apparent().altaz()[0].degrees
sun_lit = iss.at(t).is_sunlit(eph)

# 国際宇宙ステーションが見える条件の判定 
for ti, event, s_alt, s_lit in zip(t, events, sun_alt, sun_lit):
    if s_alt < -6 and s_lit==True:
        if event == 0:
            print('見え始め:', ti.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')
        if event == 1:
            print('最大仰角:', ti.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')
        if event == 2:
            print('見え終わり:', ti.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')