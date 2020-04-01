'''
G20.py

    G20 countries ,Td(Doubling time) of past 7 days.

    2020-03-24 Ichiro Yoshida
'''
G20=['Japan','S.Korea','China','Indonesia','India','SaudiArabia','France',\
     'Germany','Italy','UK','Canada','Mexico','USA','Argentina','Brazil',\
     'Russia','Turkey','SouthAfrica','Australia','Spain','Switzerland','Total:']

import csv
import os
import math
import datetime
from pytz import timezone

def case_estimate(day, case, td):
    return(case * 2**(math.log(day)/math.log(td)))
 
def Td7(case0, case1):
    return(7.0*(math.log(2.)/(math.log(case1/case0))))

dic_data={}
dic_data1={}
dic_data0={}
data = []
days=[]

now = datetime.datetime.now(timezone('UTC'))
before7 = now-datetime.timedelta(days=7.)
filename = './td7/G20'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
now_utc = now.strftime('%Y%m%d %H:%M:%S UTC')

path = './csv/'
files = os.listdir(path)
files.sort()

day0 = before7.strftime('%Y/%m/%d')
day1 = now.strftime('%Y/%m/%d')

for file in files:
    with open(path+file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        day_data = []
        while len(data):
            line = data[:1]
            for lin in line[0]:
                if('UTC' in lin):
                    date_str=lin.split(' ')[0]
            day_data.append(line[0])
            del data[:1]
        del day_data[:1]
    dic_data[date_str]=day_data

data0=dic_data[day0]
data1=dic_data[day1]

while len(data1):
    dat = data1[:1][0]
    dic_data1[dat[0].replace(' ','')]=dat
    del data1[:1]

while len(data0):
    dat = data0[:1][0]
    dic_data0[dat[0].replace(' ','')]=dat
    del data0[:1]

csvRow=[]

for country in G20:
    country1 = dic_data1.get(country)
    country0 = dic_data0.get(country)
    tot_Cases1=float(country1[1].replace(',',''))
    tot_Cases0=float(country0[1].replace(',',''))
    if(tot_Cases1 > tot_Cases0):
        if(tot_Cases1 > 10.):
            if (country1[3]):
                death_str = country1[3].replace(' ','')
                death_str2 = death_str.replace(',','')
                try:
                    deaths = float(death_str2)
                except ValueError:
                    deaths = 0.
            Td = Td7(tot_Cases0,tot_Cases1)
            days7 = case_estimate(7., tot_Cases1, Td)
            days14 = case_estimate(14., tot_Cases1, Td)
            death_rate = deaths/days14*100

            csvRow.append([country,tot_Cases0,tot_Cases1, deaths, '{:.3f}'.format(Td),\
               '{:d}'.format(int(days7)),'{:d}'.format(int(days14)), '{:.3f}'.format(death_rate)])
csvRow.sort(key=lambda x: float(x[3]), reverse=True)

print(csvRow)

with open(filename,'w',encoding='utf-8') as file:
    writer =csv.writer(file)
    writer.writerow([now_utc])
    writer.writerow(['Country',day0, day1, 'Td'])
    writer.writerows(csvRow)

