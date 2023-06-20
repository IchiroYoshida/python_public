'''
Moon Age by Skyfield
2023/06/20  Ichiro Yoshida (yoshida.ichi@gmail.com)
'''
from skyfield import api
from datetime import datetime,timedelta
from pytz import timezone
ts = api.load.timescale()
eph = api.load('de421.bsp')
from skyfield import almanac
import numpy as np


tz = timezone('Asia/Tokyo')
tj = datetime.now(tz)
print(tj)

t1 = ts.utc(tj)
t0 = ts.utc(t1.utc_datetime() - timedelta(days=30))
phase = almanac.moon_phase(eph,t1)

print('Moon phase:{:.1f} degrees'.format(phase.degrees))

t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))

t_newmoon = t[np.where( y == 0)[0][-1]]

tnj = t_newmoon.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')
ma = t1 - t_newmoon

print('前回の新月:',tnj,'JST')
print('月齢:{0:.1f}'.format(ma))
