LOCATION_TD2 = '00OSE.TD2'

from datetime import datetime
import sys
sys.path.append('./func')

import tide_day as td
import line_prn as lpr

if __name__ == '__main__':

    dr = td.DataRead(LOCATION_TD2)

    date = datetime.now()
    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    day = int(date.strftime('%d'))
    
    print (dr.name, year, month, day)

    today  = td.TideDay(dr, year, month, day)

    prn = lpr.linePrn(today)

    print(day, prn)


