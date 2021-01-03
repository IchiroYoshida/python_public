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

    ht_time  =''
    ht_level =''

    for ht in hitide_time:
        ht_time = ht_time+str(' %5s' % ht)

    print (ht_time)

    for hl in hitide_level:
        ht_level = ht_level+str(' %5s' % hl)
        
    print (ht_level)

    lw_time  =''
    lw_level =''

    for lt in lowtide_time:
        lw_time = lw_time+str(' %5s' % lt)

    print (lw_time)

    for ll in lowtide_level:
        lw_level = lw_level+str(' %5s' % ll)

    print (lw_level)

#    print('干潮時刻  = %s' % lowtide_time)
#    print('干潮潮位  = %s' % lowtide_level)

