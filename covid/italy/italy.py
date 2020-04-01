'''
  italy.py 
 
  2020-03-26 Ichiro Yoshida
'''

import math
import csv
import datetime
from pytz import timezone

population = 60.48

def td7(n0,n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

read_csv = './data/Italy.csv'
filename = './data/itlplt.csv'

csvRow = []
data = {}

with open(read_csv) as f:
    reader =csv.reader(f)
    for row in reader:
        csvRow.append(row) 

del csvRow[:2]
del csvRow[-1]

for lin in csvRow:
    date = lin[0].split('-')
    date_str = date[0]+date[1]+date[2]

    cases = int(lin[1])
    deaths = int(lin[2])

    data[date_str]=[date,cases,deaths]

days = list(data.keys())


TdRows=[]

for dd in days:
    dat = data[dd]
    year = int(dat[0][0])
    month = int(dat[0][1])
    day = int(dat[0][2])
 
    d = datetime.date(year, month, day)
    day7s = d+datetime.timedelta(days=7)
    date0 = dd
    date1 = day7s.strftime('%Y%m%d')
    date0_str = d.strftime('%Y/%m/%d')

    n0 = int(data[date0][1])

    try:
        n1 = int(data[date1][1])
        Td = td7(n0, n1)
        deaths = int(data[date0][2])
        death_Mil = deaths / population

        Td_str = '{:.3f}'.format(Td)
        death_Mil_str = '{:.3f}'.format(death_Mil)

        TdRows.append([date0_str,deaths,Td_str,death_Mil_str])

    except KeyError:
        exit

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date','deaths','Td','Deaths/Mil.'])
    writer.writerows(TdRows)
