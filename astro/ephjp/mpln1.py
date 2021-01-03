# -*- coding:utf-8 -*-

"""
月と惑星の接近  Ichiro Yoshida
2018/6/21
"""
import datetime
import ephem
import eph_func as ephf

RAD = 180. / ephem.pi
NEAR = 10.

year = 2019

moon = ephem.Moon()
sun = ephem.Sun()

mercury = ephem.Mercury()
venus = ephem.Venus()
mars = ephem.Mars()
jupiter = ephem.Jupiter()
saturn = ephem.Saturn()

location = ephem.Observer()

#location.name = '東京'
#location.lon, location.lat = '139.7414', '35.6581'

location.name = '福岡'
location.lon, location.lat = '130.391', '33.593'

location.pressure = 0
location.horizon = '-0:34'

location.elevation = 0.0

for month in range(1, 13):
    days = ephf.month_days(year, month)
    for day in range(1, days+1):
        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        #location.date = str(date0+' 9:00') #UT+9hr =JST
        location.date = str(date0)
        location.date += 15. * ephem.hour #UT+9hr =JST 0:00
        loc_date0 = location.date

        date_location = location.date
        weekday = ephf.get_weekday(date0)

        date1 = repr(ephem.localtime(location.date))
        date2 = eval(date1)
        date_str = date2.strftime('%Y%m%d')
        mm = int(date2.strftime('%m'))

        #--- 日出の時刻 -----
        today = ephf.Sun(location)
        today.sun_rise(location)
        sun_rise = today.sun_rise

        #--- 日没の時刻 -----
        today = ephf.Sun(location)
        today.sun_set(location)
        sun_set = today.sun_set

        #--- 月齢  -----
        today = ephf.Moon(location)
        today.noon(location)
        moon_age = today.moonage

        location.date = loc_date0

        moon.compute(location)
        mercury.compute(location)
        venus.compute(location)
        mars.compute(location)
        jupiter.compute(location)
        saturn.compute(location)

        moon_mercury = ephem.separation(moon, mercury) * RAD
        moon_venus = ephem.separation(moon, venus) * RAD
        moon_mars = ephem.separation(moon, mars) * RAD
        moon_jupiter = ephem.separation(moon, jupiter) * RAD
        moon_saturn = ephem.separation(moon, saturn) * RAD
         
        PRN = False

        if (moon_mercury < NEAR): 
            PRN = True
            mercury_str = str(' %4.1lf ' % moon_mercury )
        else:
            mercury_str = '  --- '

        if (moon_venus < NEAR):
            PRN = True
            venus_str = str(' %4.1lf ' % moon_venus )
        else:
            venus_str = '  --- '

        if (moon_mars < NEAR):
            PRN = True
            mars_str = str(' %4.1lf ' % moon_mars )
        else:
            mars_str = '  --- '

        if (moon_jupiter < NEAR):
            PRN = True
            jupiter_str = str(' %4.1lf ' % moon_jupiter )
        else:
            jupiter_str = '  --- '

        if (moon_saturn < NEAR):
            PRN = True
            saturn_str = str(' %4.1lf ' % moon_saturn)
        else:
            saturn_str = '  --- '

        if (PRN):
            # print(' %2d %s %s %s ' % (day, weekday, sun_rise, sun_set))
            print(' %2d %2d %s |%4.1lf | %s %s %s %s %s ' % (month, day, weekday, moon_age, mercury_str, venus_str, \
                    mars_str, jupiter_str, saturn_str ))

