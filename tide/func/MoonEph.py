'''
Moon Ephemeris: Moon Age and Tide by Skyfield
2023/06/20  Ichiro Yoshida (yoshida.ichi@gmail.com)
'''
from skyfield import api
import datetime
from pytz import timezone
ts = api.load.timescale()
eph = api.load('de421.bsp')
from skyfield import almanac
import numpy as np

tz = timezone('Asia/Tokyo')

def WeekDay(date):
    Name=['月','火','水','木','金','土','日']
    day = datetime.datetime.strptime(date,'%Y/%m/%d')
    d = day.weekday()
    return(Name[d])

#JMA:気象庁
def tidename_JMA(x):
    Name=['大', '中', '小', '長', '若', '中', '大', '中', '小', '長', '若', '中']

    if x < 36:  return(Name[0])
    elif x < 72:  return(Name[1])
    elif x < 108:  return(Name[2])
    elif x < 120:  return(Name[3])
    elif x < 132:  return(Name[4])
    elif x < 168:  return(Name[5])
    elif x < 216:  return(Name[6])
    elif x < 252:  return(Name[7])
    elif x < 288:  return(Name[8])
    elif x < 300:  return(Name[9])
    elif x < 312:  return(Name[10])
    elif x < 348:  return(Name[11])
    else : return(Name[0])

class MoonEph(object):
   def __init__(self,date):
       dt = datetime.datetime.strptime(date+' 12:00','%Y/%m/%d %H:%M') #12:00 JST
       dtj = dt.astimezone(tz)
       t1 = ts.utc(dtj)
       t0 = ts.utc(t1.utc_datetime() - datetime.timedelta(days=30))
       phase = almanac.moon_phase(eph,t1)
       self.tide_name = tidename_JMA(phase.degrees)

       t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))

       t_newmoon = t[np.where( y == 0)[0][-1]]
       self.moon_age = '{:.1f}'.format(t1 - t_newmoon)

if __name__ == '__main__':
    date = datetime.date.today().strftime('%Y/%m/%d')
    me = MoonEph(date)
    print(date)
    print(me.tide_name,' 潮')
    print('月齢＝',me.moon_age)      
