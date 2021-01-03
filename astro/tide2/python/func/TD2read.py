import numpy as np
import func.jmadata as jma

DIR   = './data/TD2/TEST/'
#FILE  = '00OSE.TD2'
#FILE = '00Yonara.TD2'
FILE = '47座間味.TD2'

file_td2=DIR+FILE

line_num = 0

pl = np.zeros(60,np.float64)
hr = np.zeros(60,np.float64)

try:
    fp = open(file_td2,'r')

except IOError as e:
    print('Cannot open %s ERR:' % file_td2,e.errno)

else:
    for line in fp:
        line1=line.replace(" ","")
        line2=line1.replace("\n","")
        line3=line2.replace("\x1a","")
        lines=line3.split(",")

        if (line_num == 0):
            name   = lines[0]
            lat0   = float(lines[1])
            lng0   = float(lines[2])
            level  = lines[3]
            line_num += 1

            lat  = int(lat0) + (lat0-int(lat0))*100/60
            lng  = int(lng0) + (lng0-int(lng0))*100/60

            #print(name, lat, lng, level)

        else:
            if (len(lines)>5):
                for k in range (60):
                    if (jma.CompSymb[k] == lines[0]):
                        key1 = k
                    if (jma.CompSymb[k] == lines[3]):
                        key2 = k

                hr[key1] = float(lines[1])
                pl[key1] = float(lines[2])
                hr[key2] = float(lines[4])
                pl[key2] = float(lines[5])
                line_num += 1
         
            else:
                exit

    fp.close()

"""
    print(name, lat, lng, level)

    for n in range(60):
        print(jma.CompSymb[n], hr[n], pl[n])
"""
