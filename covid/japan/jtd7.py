'''
  Td(Doubling time for 7 days) of Japan

  2020-03-26 Ichiro Yoshida
'''
import math
import csv
import os
import datetime

dic_data={}
dic_data1={}
dic_data0={}
data = []
days = []

now = datetime.datetime.now()
before7 = now - datetime.timedelta(days=7.)
filename = './td7/td7'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
now_jst = now.strftime('%Y%m%d %H:%M:%S JST')

path = './jdata/'
files = os.listdir(path)
files.sort()

day0 = before7.strftime('%Y/%m/%d')
day1 = now.strftime('%Y/%m/%d')

def td7(n0,n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

def kval(n0,n1):   #Takashi Nakano Osaka.Univ.
    return(1-n0/n1)

for file in files:
    with open(path+file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        day_data = []
        while len(data):
            line = data[:1]
            for lin in line[0]:
                if('JST' in lin):
                    date_str=lin.split(' ')[0]
            day_data.append(line[0])
            del data[:1]
        del day_data[:1]
    dic_data[date_str]=day_data

data0 = dic_data[day0]
data1 = dic_data[day1]
for dat in data0:
    dic_data0[dat[0]]=dat
for dat in data1:
    dic_data1[dat[0]]=dat

prefs = dic_data0.keys()
total0 = 0
total1 = 0
csvRow = []
for pref in prefs:
    pref0 = dic_data0.get(pref)
    pref1 = dic_data1.get(pref)
    cases0 = float(pref0[1])
    total0 += cases0
    cases1 = float(pref1[1])
    total1 += cases1

    if(cases0):
        if(cases0<cases1):
            d7 = '{:.3f}'.format(td7(cases0, cases1))
            k  = '{:.3f}'.format(kval(cases0, cases1))
            csvRow.append([pref,cases0,cases1,d7,k])
        else:
            k  = '{:.3f}'.format(kval(cases0, cases1))
            csvRow.append([pref,cases0,cases1,1000,k])
    else:
        csvRow.append([pref,cases0,cases1,1000,0])

total_d7 = '{:.3f}'.format(td7(total0, total1))
total_k  = '{:.3f}'.format(kval(total0, total1))

csvRow.append(['全国',total0, total1,total_d7,total_k])
csvRow.sort(key=lambda x:float(x[3]))
print(now_jst)
with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([now_jst])
    writer.writerow(['都道府県',day0,day1,'Td','K'])
    writer.writerows(csvRow)

