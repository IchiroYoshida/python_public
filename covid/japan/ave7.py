'''
 Cases of the average 7 days of Japan 

 2020-05-03 Ichiro Yoshida
'''

import math
import csv
import os
import datetime

def td7(n0, n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

dic_data={}
dic_data0={}
dic_data1={}
dic_ave7={}

data = []
days = []

path = './jdata/'
files = os.listdir(path)
files.sort()

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

days = list(dic_data.keys())
days0 = dic_data[days[0]]
for d in days0:
    dic_data0[d[0]]=d
prefs = dic_data0.keys() 

while(len(days)>6):
    days7 = days[:7]
    days_val = days[3]

    sum_pref = {}
    tmp_pref = {}

    for day in range(7):
        if (day):
            day_data = dic_data[days7[day]]
            for dd in day_data:
                tmp_pref[dd[0]] = float(dd[1])

            for pref in prefs:
                pref_dat = tmp_pref.get(pref)
                pref_sum = sum_pref.get(pref)
                sum_pref[pref] = pref_dat + pref_sum
        else:
            day_data = dic_data[days7[day]]
            for dd in day_data:
                sum_pref[dd[0]] = float(dd[1])

    for pref in prefs:
        pref_dat = sum_pref.get(pref)
        sum_pref[pref] = pref_dat/7.

    dic_ave7[days_val]=list(sum_pref.items())
    del days[:1]

days = list(dic_data.keys())

n = len(days)
data0 = []
data1 = []
dic_data0 = {}
dic_data1 = {}

'''
#------------ Average 7 days ---------------
for d in range(3,n-10):
    day0=days[d]
    day1=days[d+7]
    day_str =day0.split('/')
    file_day = day_str[0][-2:]+day_str[1]+day_str[2]
    file_name = './ave7/Ave7_'+file_day+'.csv'

    data0 = dic_ave7[day0]
    data1 = dic_ave7[day1]

    for dat in data0:
        dic_data0[dat[0]]=dat
    for dat in data1:
        dic_data1[dat[0]]=dat

    total0=0
    total1=0
    csvRow = []

    for pref in prefs:

        pref0 = dic_data0.get(pref)
        pref1 = dic_data1.get(pref)
        cases0 = float(pref0[1])
        total0 += cases0
        cases1 = float(pref1[1])
        total1 += cases1

        if(cases0):
            if(cases0 < cases1):
                d7 = '{:.3f}'.format(td7(cases0, cases1))
                csvRow.append([pref,'{:.3f}'.format(cases0), '{:.3f}'.format(cases1), d7])
            else:
                csvRow.append([pref,'{:.3f}'.format(cases0), '{:.3f}'.format(cases1), 1000])

    total_d7 = '{:.3f}'.format(td7(total0, total1))
    csvRow.append(['全国','{:.3f}'.format(total0),'{:.3f}'.format(total1), total_d7])
    csvRow.sort(key=lambda x:float(x[3]))

    with open(file_name,'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['都道府県',day0,day1,'Td'])
        writer.writerows(csvRow)
'''

#----------- Prefs. Td7 --------------
for pref in prefs:
    csvRow = []
    file_name = './pref7/Pref7_'+pref+'.csv'
    for d in range(3, n-10):
        day0 = days[d]
        day1 = days[d+7]
        day_val = days[d+3]

        data0 = dic_ave7[day0]
        data1 = dic_ave7[day1]

        for dat in data0:
            dic_data0[dat[0]]=dat
        for dat in data1:
            dic_data1[dat[0]]=dat

        pref0 = dic_data0.get(pref)
        pref1 = dic_data1.get(pref)
        cases0 = float(pref0[1])
        cases1 = float(pref1[1])

        if(cases0):
            if(cases0 < cases1):
                d7 = '{:.3f}'.format(td7(cases0, cases1))
                csvRow.append([day_val,d7])
            else:
                csvRow.append([day_val,1000])

        #csvRow.sort(key=lambda x:float(x[1]))

    with open(file_name,'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([pref,'Td'])
        writer.writerows(csvRow)

