import sys
import math
import ephem
import datetime
import tide_func
from moon_calc import *
import numpy as np
import data_read
"""
ヨナラ水道　年間潮流表(TEX)
"""
year = 2016

print('\\documentclass[12pt.a4j]{jsarticle}')
print('\\usepackage{lscape}')

print('\\begin{document}')
print('\\pagestyle{empty}')
print('\\begin{landscape}')
print('\\begin{center}')

pt = tide_func.Port()

pt.hr = np.zeros(60,np.float64)
pt.pl = np.zeros(60,np.float64)

pt.name = 'ヨナラ水道'
pt.lat  = data_read.lat
pt.lng  = data_read.lng
pt.level= data_read.level

pt.hr   = data_read.hr
pt.pl   = data_read.pl

moon = ephem.Moon()
pt_eph = ephem.Observer()
pt_eph.lon = pt.lng
pt_eph.lat = pt.lat
pt_eph.elevation = 0.0

for month in range(1,13):
   days = tide_func.month_days(year,month)

   print('\\begin{table}[ht]')
   print('\\scalebox{0.8}{')
   
   print('   \\begin{tabular*}{250mm}{|rc|cr|rrrrrrrrrrrrrrrrrrrrrrrr|}')

   hrs=' 0'
   for hr in range(1,24):
       hrs +=str('&%2d' % hr)

   print('   \\multicolumn{2}{c}{ %4d 年} & \\multicolumn{2}{c}{ %2d 月} & \\multicolumn{24}{c}{    %s  潮流表　南から北方向への流れを＋表示　　【暫定版】　（0-24時） } \\\\' % (year,month,pt.name))

   print('\\hline')
   print('   \\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{2}{c|}{潮（月齢）}&%s\\\\' % hrs)
   print('\\hline')

   for d in range(1,days+1):

      pt.date = str(year)+str('/%02d' % month)+str('/%02d' % d)
      pt_eph.date = str(pt.date+' 9:00')

      date_prn = str(pt.date)
      weekday  = get_weekday(pt.date)

      today_moon = Moon(pt_eph)
      today_moon.noon(pt_eph)

      moon_prn = today_moon.tname+str('&%4.1f' % today_moon.moonage)

      today = tide_func.Tide(pt)
      today.wav(pt)

      current = today.m2s2

      cur  = (current[0:72:3]+6)/15

      prn=str('%+2d' % int(round(cur[0])))

      for c in range(1,24):
         prn += str('&%+2d' % round(cur[c]))

      print('%2d & %s & %s & %s \\\\' % (d,weekday,moon_prn,prn))

   print('  \\hline')
   print('  \\end{tabular*}')
   print('  }')
   print('\\end{table}')
   print('\\newpage')

print('\\end{center}')
print('\\end{landscape}')
print('\\end{document}')

