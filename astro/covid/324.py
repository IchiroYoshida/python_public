import csv

read_file = './csv/covid20200324_140404.csv'
write_file = 'test'

data = []

with open(read_file) as f:
    data = f.read()
    data.split(',')

for d in data:
    print(d)

'''    
while len(data):
    row = data[:11]
    country = row[0]
    tot_Case = float(row[1].replace(',',''))
    if (len(row[3])>1):
        tot_Death = float(row[3].replace(',',''))
        if len(row[8]):
            case_Mil = float(row[8].replace(',',''))
            death_Mil = '{:.3f}'.format(tot_Death * case_Mil /tot_Case)
            csvRow.append([country, death_Mil])
    del data[:11]

csvRow.sort(key=lambda x: float(x[1]), reverse=True )
print(now_utc)

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country','Deaths/Mil.',now_utc])
    writer.writerows(csvRow)
'''

