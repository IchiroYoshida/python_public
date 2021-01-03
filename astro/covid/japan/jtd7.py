'''
  Td(Doubling time for 7 days) of Japan

  2020-03-26 Ichiro Yoshida
'''
import math
import csv

def td7(n0,n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

read_csv = './jdata/AREA1.csv'
filename = './jdata/Td7Japan.csv'

csvRow = []

with open(read_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        csvRow.append([row])

del csvRow[:1]

Row=[]
for lin in csvRow:
    pref = lin[0][0]
    case = int(lin[0][1])
    case0 = int(lin[0][3])
    if (case0>1):
        if(case>case0):
            td = td7(case0,case)
            Row.append([pref,case0,case,td])

Row.sort(key=lambda x:float(x[3]), reverse=True)

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['都道府県','3/18','3/25','Td'])
    writer.writerows(Row)

