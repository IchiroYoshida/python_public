from skyfield.api import Topos, load
from datetime import timedelta
from pytz import timezone

# 時刻設定
ts = load.timescale()
t = ts.utc(2000,1,1,7,20,0)
#t0 = ts.now()
#t1 = ts.utc(t0.utc_datetime() + timedelta(days=10))
tz = timezone('Asia/Tokyo')

# 天体暦設定
eph = load('de421.bsp')
sun, earth = eph['sun'], eph['earth']

# 観測地設定
tokyo = Topos('33.6544 N', '139.7447 E')

astrometric = (earth + tokyo).at(t).observe(sun)

# 太陽高度の計算
sun_app= astrometric.apparent()  #.altaz()[0].degrees
sun_ra, sun_dec, sun_r = astrometric.radec()
#sun_alt = sun_app.altaz()[0].degrees

sun_alt, sun_az, distance = sun_app.altaz()

RA = '{:.8f}'.format(sun_ra._degrees)
DEC = '{:.8f}'.format(sun_dec._degrees)
print(RA, DEC, sun_r,sun_alt, sun_az)
