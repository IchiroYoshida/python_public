from skyfield.api import load, Topos
from skyfield.almanac import find_discrete, sunrise_sunset
from datetime import timedelta
from pytz import timezone

ts = load.timescale()
eph = load('de421.bsp')

#t0 = ts.now()
t0 = ts.utc(2022,12,31,21,0) #UTC ->JST 1.1 6:00 AM
t1 = ts.utc(t0.utc_datetime() + timedelta(days=1))
tz = timezone('Asia/Tokyo')

position = Topos('35.6925 N', '140.8656 E')

t, updown = find_discrete(t0, t1, sunrise_sunset(eph, position))

for yi, ti in zip(updown, t):
    print('次の日の出:' if yi else '次の日の入り:', ti.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S'), 'JST')
