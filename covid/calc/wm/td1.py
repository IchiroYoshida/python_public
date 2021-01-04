import csv
import os
import math
import datetime
from pytz import timezone

dic_data={}
dic_data1={}
dic_data0={}
data = []
days=[]

now = datetime.datetime.now(timezone('UTC'))
#filename = './td7/td'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
filename = './td7/td20200322.csv'

now_utc = now.strftime('%Y%m%d %H:%M:%S UTC')

path = './csv/'
files = os.listdir(path)
files.sort()

day0 = '2020/03/15'
day1 = '2020/03/22'

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

countries = dic_data0.keys()
csvRow=[]

for country in countries:
    country1 = dic_data1.get(country)
    country0 = dic_data0.get(country)
    tot_Cases1=float(country1[1].replace(',',''))
    tot_Cases0=float(country0[1].replace(',',''))
    if(tot_Cases1 > tot_Cases0 ):
        if(tot_Cases1 > 10.):
            Td = '{:.3f}'.format(7.0 * math.log(2)/math.log(tot_Cases1/tot_Cases0))
            csvRow.append([country,tot_Cases0,tot_Cases1,Td])
csvRow.sort(key=lambda x: float(x[3]), reverse=True)

print(now_utc)
with open(filename,'w',encoding='utf-8') as file:
    writer =csv.writer(file)
    writer.writerow([now_utc])
    writer.writerow(['Country','3/15','3/22','Td'])
    writer.writerows(csvRow)
