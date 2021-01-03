"""
年間潮時表（TEX版)
2018/05/26
"""

from datetime import datetime
import sys
sys.path.append('./func')

import tide_day as td
import tide_func as tf
import line_tex as ltex

#LOCATION_TD2 = '00OSE.TD2'
LOCATION_TD2 = '00Hatoma.TD2'

year = 2018

if __name__ == '__main__':

    dr = td.DataRead(LOCATION_TD2)

    print("\\documentclass[12pt.a4j]{jsarticle}")
    print("\\begin{document}")
    print("\\pagestyle{empty}")
    print("\\begin{center}")

    for month in range (1, 13):
        days = tf.month_days(year, month)
  
        print("{\\LARGE %s  潮汐表　　　}" % dr.name)
        print("{\\large %4d 年 %2d 月}\\\\" %(year,month))
        print("\\begin{table}[ht]")
        print("\\begin{tabular}{|rc|cr|ccrccr|ccrccr|}")
        print("\\hline")
        print("\\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{2}{c|}{潮（月齢）} & \\multicolumn{6}{c|}{満潮時刻　―　潮位(cm)} & \\multicolumn{6}{c|}{干潮時刻　―　潮位(cm)} \\\\")
        print("\\hline")

        for day in range(1, days+1):

            today  = td.TideDay(dr, year, month, day)

            print('{0:2d} &'.format(day), ltex.lineTex(today))

        print("\\hline")
        print("\\end{tabular}")
        print("\\end{table}")
        print("\\newpage")

    print("\\end{center}")
    print("\\end{document}")
