'''
  countries.csv -> CSV2 
 
  2020-05-06 Ichiro Yoshida
'''
import pomberCountry as pc
import worldPop as wp

import math
import csv
import os

def td7(n0,n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

path = './data/csv/'

files = os.listdir(path)
files.sort()

for file in files:
    country0 = file.split('.')[0]
    try:
        country1 = pc.countries[country0][0]
    except KeyError:
        continue

    csv_data = []
    with open(path+file) as f:
        reader = csv.reader(f)
        for row in reader:
            csv_data.append(row)
    del csv_data[0]

    data = {}
    for dat in csv_data:
        date = dat[0].split('-')
        date_str = date[0]+'{0:02d}'.format(int(date[1]))+'{0:02d}'.format(int(date[2]))
        cases  = int(dat[1])
        deaths = int(dat[2])
        data[date_str]=[cases,deaths]

    days = list(data.keys())
    data1={}
    #-------- daily delta cases,deaths -------
    for dd in range(1,len(days)-1):
        day0 = days[dd]
        dat0 = data[day0]

        day1 = days[dd+1]
        dat1 = data[day1]
    
        case_day = int(dat1[0])-int(dat0[0])
        death_day = int(dat1[1])-int(dat0[1])

        data1[day1]=[dat1[0],case_day,dat1[1],death_day]

    days = list(data1.keys())
    data2 ={}
    #---------- daily data -> 7days ave. -------------
    while(len(days)>6):
        days7 = days[:7]
        days_val = days7[3]

        tot_case = 0
        day_case = 0
        tot_death = 0
        day_death = 0

        for day in range(7):
            day_data = data1[days7[day]]
            tot_case += int(day_data[0])
            day_case += int(day_data[1])
            tot_death += int(day_data[2])
            day_death += int(day_data[3])

        tot_case /= 7.
        day_case /= 7.
        tot_death /= 7.
        day_death /= 7.

        day_data = data1[days_val]
        data2[days_val]=[day_data[0],
                '{:.2f}'.format(tot_case),
                day_data[1],
                '{:.2f}'.format(day_case),
                day_data[2],
                '{:.2f}'.format(tot_death),
                day_data[3],
                '{:.2f}'.format(day_death)]

        del days[:1]

    days = list(data2.keys())

    data3 = {}
    #----------------- calc. Td7(Ave)----------------
    for dd in range(len(days)-7):
        day0 = days[dd]
        day1 = days[dd+7]

        dat0 = data2[day0]
        dat1 = data2[day1]

        case0 = float(dat0[1])
        case1 = float(dat1[1])

        if(case0):
            if(case0 < case1):
                Td7 = '{:.2f}'.format(td7(case0, case1))
            else:
                Td7 = 'NG'
        else:
            Td7 = 'NG'
        
        try:
            pop = int(wp.countries[country1][0])
        except KeyError:
            continue

        popM = pop/1000000
        deathM = float(dat0[5])/popM
        data3[day0]=[Td7,dat0[0],dat0[1],dat0[2],dat0[3],dat0[4],dat0[5],dat0[6],dat0[7],deathM]
    #--------------- Format and Write --------
    days = list(data3.keys())

    csvRow = []

    for dd in range(len(days)):
        day0 = days[dd]

        year = day0[:4]
        month = day0[4:6]
        day  = day0[6:8]
        day_str = year+'/'+month+'/'+day

        data0 = data3[day0]

        line = []
        line.append(day_str)

        for d in data0:
            line.append(d)

        csvRow.append(line)

    filename = './data/csv2/'+country1+'.csv'
    with open(filename,'w',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Td','Cases(Tot.)','Cases(7Ave.)','Cases(Day)','Cases(7Ave.Day)',\
                                 'Deaths(Tot.)','Death(7Ave.)','Death(Day)','Death(7Ave.Day)','Death/Mil.pop(7Ave.Day)'])
        writer.writerows(csvRow)


