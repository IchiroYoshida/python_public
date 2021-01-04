'''
  italy2.py 
 
  2020-05-05 Ichiro Yoshida
'''
import math
import csv

def td7(n0,n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

read_csv = './data/Italy.csv'
filename = './data/Itdata.csv'

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

    Td7 = '{:.2f}'.format(td7(case0, case1))

    data3[day0]=[Td7,dat0[0],dat0[1],dat0[2],dat0[3],dat0[4],dat0[5],dat0[6],dat0[7]]

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

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date','Td','Cases(Tot.)','Cases(7Ave.)','Cases(Day)','Cases(7Ave.Day)',\
                                 'Deaths(Tot.)','Death(7Ave.)','Death(Day)','Death(7Ave.Day)'])
    writer.writerows(csvRow)
