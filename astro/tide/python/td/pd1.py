import os

DIR  = '/Users/ichiro3/git/test0126/tide/python/td/TD2/TEST/'
FILE = '47尖閣 魚釣島.TD2'

file_td2=DIR+FILE
file_td='./test.td'

#分潮の略号と番号

TideName  = { 'Sa': 1, 'Ssa': 2,  'Mm': 3, 'MSf': 4,  'Mf': 5, '2Q1': 6, \
            'Sig1': 7,  'Q1': 8,'Rho1': 9,  'O1':10, 'MP1':11,  'M1':12, \
            'Chi1':13, 'Pi1':14,  'P1':15,  'S1':16,  'K1':17,'Psi1':18, \
            'Phi1':19,'The1':20,  'J1':21, 'SO1':22, 'OO1':23, 'OQ2':24, \
            'MNS2':25, '2N2':26, 'Mu2':27,  'N2':28, 'Nu2':29, 'OP2':30, \
              'M2':31,'MKS2':32,'Lam2':33,  'L2':34,  'T2':35,  'S2':36, \
              'R2':37,  'K2':38,'MSN2':39, 'KJ2':40,'2SM2':41, 'MO3':42, \
              'M3':43, 'SO3':44, 'MK3':45, 'SK3':46, 'MN4':47,  'M4':48, \
             'SN4':49, 'MS4':50, 'MK4':51,  'S4':52, 'SK4':53,'2MN6':54, \
              'M6':55,'MSN6':56,'2MS6':57,'2MK6':58,'2SM6':59,'MSK6':60 }

line_num = 0

tn=['']*60
hr=[0]*60
pl=[0]*60


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
                key1 = TideName[lines[0]]
                key2 = TideName[lines[3]]

                tn[key1-1] = lines[0]
                hr[key1-1] = lines[1]
                pl[key1-1] = lines[2]
                tn[key2-1] = lines[3]
                hr[key2-1] = lines[4]
                pl[key2-1] = lines[5]
                line_num += 1
         
            else:
                exit

    fp.close()
"""
try:
    fp60 = open(file_td,'w')
except IOError as e:
    print('Cannot open file %s Error %d' % file_td,e.errno)
else:
    fp60.write("pt.name = %s\n" % name)
    fp60.write("pt.lat  = %s\n" % lat)
    fp60.write("pt.lon  = %s\n" % lon)
    fp60.write("pt.level= %s\n" % level)
            
    for i in range(60):
        fp60.write("pt.pl[%d]  = %6.2f    # %s \n" %(i,float(pl[i]),TideName[i+1]))

    for i in range(60):
        fp60.write("pt.hr[%d]  = %6.2f    # %s \n" %(i,float(hr[i]),TideName[i+1]))

    fp60.close()
"""

