LOCATION_TD2 = '00OSE.TD2'

from datetime import datetime
import sys
sys.path.append('./func')

import tide_day as td
import tide_func as tf
import line_prn as lpr

if __name__ == '__main__':

    dr = td.DataRead(LOCATION_TD2)

    date = datetime.now()
    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    days = tf.month_days(year, month)
    
    print (dr.name, year, month)

    for day in range(1, days+1):

        today  = td.TideDay(dr, year, month, day)

        print('{0:2d}'.format(day), lpr.linePrn(today))
