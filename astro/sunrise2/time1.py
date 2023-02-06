from datetime import datetime
from pytz import timezone, utc
import matplotlib.pyplot as plt
from skyfield.api import load,Topos

ts = load.timescale()
tz = timezone('Asia/Tokyo')

eph = load('de421.bsp')
pos = Topos('35.6925 N', '140.8656 E')

when = '2023-01-01 06:30:00' #JST

dt = datetime.strptime(when, '%Y-%m-%d %H:%M:%S')
print(dt)
'''
local_dt = tz.localize(dt, is_dst=None)
utc_dt = local_dt.astimezone(utc)

ts =load.timescale()
t=ts.from_datetime(utc_dt)

utc_time = t.utc_strftime()
jst_time = local_dt.strftime()

print(utc_time,jst_time)
'''
