import os

DIR  = '/Users/ichiro3/git/test0126/tide/python/td/TD2/TEST/'
FILE = '47尖閣 魚釣島.TD2'

file_td2=DIR+FILE
file_td40='./test.td40'

line_num = 0

tn=['']*40
hr=[0]*40
pl=[0]*40


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
            name  = lines[0]
            lat   = lines[1]
            lon   = lines[2]
            level = lines[3]
            line_num += 1

        else:
            if (len(lines)>5):
                tn[line_num*2-2] = lines[0]
                hr[line_num*2-2] = lines[1]
                pl[line_num*2-2] = lines[2]
                tn[line_num*2-1] = lines[3]
                hr[line_num*2-1] = lines[4]
                pl[line_num*2-1] = lines[5]
                line_num += 1
         
            else:
                exit

                #fp.close()

try:
    fp40 = open(file_td40,'w')
except IOError as e:
    print('Cannot open file %s Error %d' % file_td40,e.errno)
else:
    fp40.write("pt.name = %s\n" % name)
    fp40.write("pt.lat  = %s\n" % lat)
    fp40.write("pt.lon  = %s\n" % lon)
    fp40.write("pt.level= %s\n" % level)
            
    for i in range(40):
        fp40.write("pt.pl[%d]  = %6.2f    # %s \n" %(i,float(pl[i]),tn[i]))

    for i in range(40):
        fp40.write("pt.hr[%d]  = %6.2f    # %s \n" %(i,float(hr[i]),tn[i]))

    fp40.close()
