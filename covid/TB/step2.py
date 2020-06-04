'''
 Create DeMil.csv from Worldmeters Deaths./Mil.pop csv(DeMilWM.csv)

 2020-06-04
'''

import csv
import abb3 as ab3

file_CSV = './TBC2018.csv'
file_DeMil = './DeMilWM.csv'
outfile = './DeMilTBC2018.csv'

data_CSV = []
data_DeMil = []

dic_CSV = {}
dic_DeMil = {}

with open(file_CSV) as f:
    reader = csv.reader(f)
    for row in reader:
        data_CSV.append(row)

for dat in data_CSV:
    dic_CSV[dat[1]]=dat[2]

with open(file_DeMil) as f:
    reader = csv.reader(f)
    for row in reader:
        data_DeMil.append(row)

for dat in data_DeMil:
    try:
        code = ab3.countries[dat[0]][0]
        val = dat[1]
        dic_DeMil[code] = val 
    except KeyError:
        continue

codes = list(dic_DeMil.keys())
csvRow = []

for code in codes:
    try:
        DeMil = dic_DeMil[code]
        TBC   = dic_CSV[code]
        country = ab3.codes[code]
        if(TBC):
            csvRow.append([country,code,TBC,DeMil])
    except KeyError:
        continue

with open(outfile, 'w', encoding='utf=8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country','Country Code','TBC','Deaths/Mil.pop.'])
    writer.writerows(csvRow)
