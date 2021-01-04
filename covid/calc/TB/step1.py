import csv

filename = './TBC.csv'
outfile  = './TBC2018.csv'

data = []
csvRow = []
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

for dat in data:
    code = ''
    value = ''
    for d in range(len(dat)):
        if (d==1):
            country=dat[0]
            code = dat[d]
        elif(d==62):
            value = dat[d]
    csvRow.append([country,code,value])

del csvRow[:5]

with open(outfile,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csvRow)
