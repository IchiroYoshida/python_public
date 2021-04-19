import csv

file = './HIP1000.csv'

with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        Number = row[0].split(' ')[1]
        Mag = row[1]
        Ra = row[2]
        Dec = row[3]
        BV = row[4]
        prn = "    "+"HIP"+Number+":{Mag:"+Mag+",Ra:"+Ra+",Dec:"+Dec+",BV:"+BV+"},"
        print(prn)
        
        


