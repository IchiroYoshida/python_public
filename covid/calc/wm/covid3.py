'''
covid3.py

    Td(doubling time) of past 7 days and death/Mil.population.

    2020-06-04 Ichiro Yoshida
'''

import csv
import os
import math
import datetime
from pytz import timezone

def Td7(case0, case1):
    return(7.*(math.log(2.)/(math.log(case1/case0))))

dic_data={}
dic_data0={}
dic_data1={}
data = []
days = []

now = datetime.datetime.now(timezone('UTC'))
before7 = now-datetime.timedelta(days=7.)
filename = './td7/Mil'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
now_utc = now.strftime('%Y/%m/%d %H:%M:%S UTC')

path = './csv/'
files = os.listdir(path)
files.sort()

day0 = before7.strftime('%Y%m%d')
day1 = now.strftime('%Y%m%d')

for file in files:
    date_str = file.split('_')[0].replace('covid','')
    data = []
    with open(path+file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        del data[:8]
        dic_data[date_str]=data

data0 = dic_data[day0]
data1 = dic_data[day1]

for dd in data0:
    dic_data0[dd[0]]=dd

for dd in data1:
    dic_data1[dd[0]]=dd

countries = list(dic_data0.keys())
csvRow = []

for country in countries:
    country0 = dic_data0.get(country)
    country1 = dic_data1.get(country)
    tot_Cases0 = float(country0[1].replace(',',''))
    try:
        tot_Cases1 = float(country1[1].replace(',',''))

    except TypeError:
        print('tot_Cases1 TypeError!')
        #pass 

    if(country1[3]):
        death_str = country1[3].replace(' ','')
        death_str2 = death_str.replace(',','')
        try:
            tot_Death = float(death_str2)
        except ValueError:
            tot_Death = 0.

    if(country1[8]):
        section = country1[13]
        case_Mil_str = country1[8].replace(' ','')
        case_Mil_str2 = case_Mil_str.replace(',','')
        try:
            case_Mil = float(case_Mil_str2)
        except ValueError:
            case_Mil = 0.

        if(case_Mil):
            if(tot_Cases1 > tot_Cases0):
                if(tot_Death > 1.):
                    Td = Td7(tot_Cases0, tot_Cases1)
                    Mil_pop = tot_Cases1 / case_Mil
                    death_Mil = tot_Death / Mil_pop
                    csvRow.append([section,country,'{:d}'.format(int(tot_Death)), '{:5.3f}'.format(Td),'{:5.3f}'.format(death_Mil)])

csvRow.sort(key=lambda x: float(x[4]), reverse=True )
print(now_utc)

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([now_utc])
    writer.writerow(['Continent','Country','Total deaths','Td','Deaths/Mil.'])
    writer.writerows(csvRow)
