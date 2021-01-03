import sys
import tide
import numpy as np

"""
月間潮時表
2016/08/13
"""

table_month = '2016/09'

year  = int(table_month.split('/')[0])
month = int(table_month.split('/')[1])

days = tide.month_days(year,month)

for d in range(0,days):
    from port_data.hakata_data import *

    day = d+1
    pt.date = str(year)+str('/%02d' % month)+str('/%02d' %day)

    print (pt.date)

    today = tide.Tide(pt)
    tt= today.tide(pt)

    level  = today.tl
    tide   = today.tide
    hitide = today.hitide
    lowtide= today.lowtide

    hitide_time   = np.array(hitide)[:,0]
    hitide_level  = np.array(hitide)[:,1]

    lowtide_time  = np.array(lowtide)[:,0]
    lowtide_level = np.array(lowtide)[:,1]

    print('満潮時刻  = %s' % hitide_time)
    print('満潮潮位  = %s' % hitide_level)

    print('干潮時刻  = %s' % lowtide_time)
    print('干潮潮位  = %s' % lowtide_level)

