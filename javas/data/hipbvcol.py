import csv

file = './HIP1000.csv'

def bv2rgb(bv):
    if (bv<-0.4):
        bv=-0.4
    if (bv> 2.0):
        bv= 2.0
    
    r = 0.0
    g = 0.0
    b = 0.0

    if (bv>=-0.40) & (bv<0.00):
        t=(bv+0.40)/(0.00+0.40)
        r=0.61+(0.11*t)+(0.1*t*t)
    elif (bv>= 0.00) & (bv<0.40):
        t=(bv-0.00)/(0.40-0.00)
        r=0.83+(0.17*t) 
    elif (bv>= 0.40) & (bv<2.10):
        t=(bv-0.40)/(2.10-0.40)
        r=1.00

    if (bv>=-0.40) & (bv<0.00):
        t=(bv+0.40)/(0.00+0.40)
        g=0.70+(0.07*t)+(0.1*t*t)
    elif (bv>= 0.00) & (bv<0.40):
        t=(bv-0.00)/(0.40-0.00)
        g=0.87+(0.11*t)    
    elif (bv>= 0.40) & (bv<1.60):
        t=(bv-0.40)/(1.60-0.40)
        g=0.98-(0.16*t)
    elif (bv>= 1.60) & (bv<2.00):
        t=(bv-1.60)/(2.00-1.60)
        g=0.82-(0.5*t*t)
    if (bv>=-0.40) & (bv<0.40):
        t=(bv+0.40)/(0.40+0.40)
        b=1.00
    elif (bv>= 0.40) & (bv<1.50):
        t=(bv-0.40)/(1.50-0.40)
        b=1.00-(0.47*t)+(0.1*t*t)
    elif (bv>= 1.50) & (bv<1.94):
        t=(bv-1.50)/(1.94-1.50)
        b=0.63-(0.6*t*t)
    
    R = format(int(r*255),'2X')
    G = format(int(g*255),'2X')
    B = format(int(b*255),'2X')

    str = '#'+R+G+B
    return(str)

with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        Number = row[0].split(' ')[1]
        Mag = row[1]
        Ra = row[2]
        Dec = row[3]
        BV = row[4]
        bv = float(BV)
        rgb = bv2rgb(bv)

        prn = "    "+"HIP"+Number+":{Mag:"+Mag+",Ra:"+Ra+",Dec:"+Dec+",BV:'"+rgb+"'},"
        print(prn)
        
        


