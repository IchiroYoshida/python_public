import csv

file = './OpenClust.csv'

with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        Name= row[0].replace(' ','')
        Ra = row[1]
        Dec = row[2]
        prn = "\t"+Name+":{Ra:"+Ra+",Dec:"+Dec+"},"
        print(prn)
        
        

