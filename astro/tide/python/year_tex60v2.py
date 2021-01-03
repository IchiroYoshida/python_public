import sys
import math
import ephem
import datetime
import tide_func 
from moon_calc import *
import numpy as np

"""
年間潮時表
2018/12/24
"""
year = 2018

print("\\documentclass[12pt.a4j]{jsarticle}")
print("\\begin{document}")
print("\\pagestyle{empty}")
print(" \\begin{center}")

for month in range(1, 13):
    from port_data.ishigaki_data60 import *

    days = tide_func.month_days(year, month)

    print(" {\\LARGE %s　潮汐表　　　}" % pt.name )
    print(" {\\large %4d 年 %2d 月}\\\\" %(year,month))
    print(" \\begin{table}[ht]")
    print("    \\begin{tabular}{|rc|cr|ccrccr|ccrccr|}")
    print("    \\hline")
    print("    \\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{2}{c|}{潮（月齢）} & \\multicolumn{6}{c|}{満潮時刻　―　潮位(cm)} & \\multicolumn{6}{c|}{干潮時刻　―　潮位(cm)} \\\\")
    print(" \\hline")

    for d in range(0,days):
        from port_data.ishigaki_data60 import *

        moon=ephem.Moon()

        pt_eph=ephem.Observer()
        pt_eph.lon, pt_eph.lat = pt.lng,pt.lat
        pt_eph.elevation = 0.0

        day = d+1

        pt.date = str(year)+str('/%02d' % month)+str('/%02d' % day)
        pt_eph.date = str(pt.date+' 9:00')

        date_prn = str(pt.date)
        weekday  = get_weekday(pt.date)

        today_moon = Moon(pt_eph)
        today_moon.noon(pt_eph)

        moon_prn = today_moon.tname+str(' & %4.1f' % today_moon.moonage)

        today = tide_func.Tide(pt)
        today.wav(pt)

        level  = today.tl
        tide   = today.tide
        hitide = today.hitide
        lowtide= today.lowtide

        hitide_time   = np.array(hitide)[:,0]
        hitide_level  = np.array(hitide)[:,1]

        hitide_prn  = []
        lowtide_prn = []

        for hi in hitide:
           hitide_prn.append(str(' %5s &-& %3s '%(hi[0],hi[1])))
 
        for lo in lowtide:
           lowtide_prn.append(str(' %5s &-& %3s '%(lo[0],lo[1])))


        if len(hitide_prn) < 2 :
            hitide_prn.append(' --:-- &-&~~~~~')

        if len(lowtide_prn) < 2 :
           lowtide_prn.append(' --:-- &-&~~~~~')

        print("%2d & %s & %s & %s & %s &  %s &  %s \\\\" %(day,weekday,moon_prn,hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1]))

    print("   \\hline")
    print("   \\end{tabular}")
    print("\\end{table}")
    print("\\newpage")


print("\\end{center}")
print("\\end{document}")
