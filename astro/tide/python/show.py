import os

#DIR  = './td/TD2/TEST/'
#FILE = '47尖閣 魚釣島.TD2'
DIR   = './td/TD2/8.KYUSHU1/'
FILE  = './41仮屋.TD2'

file_td2=DIR+FILE
#file_td='./test.td'

#分潮の略号と番号

TideName  = ['Sa','Ssa','Mm','MSf','Mf','2Q1','Sig1','Q1','Rho1','O1','MP1','M1', \
            'Chi1','Pi1','P1','S1','K1','Psi1','Phi1','The1','J1','SO1','OO1','OQ2', \
            'MNS2','2N2','Mu2','N2','Nu2','OP2','M2','MKS2','Lam2','L2',\
            'T2','S2','R2','K2','MSN2','KJ2','2SM2','MO3','M3','SO3',\
            'MK3','SK3', 'MN4','M4','SN4','MS4','MK4','S4','SK4','2MN6',\
            'M6','MSN6','2MS6','2MK6','2SM6','MSK6']

line_num = 0

hr=[0.]*60
pl=[0.]*60

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
                for k in range (60):
                    if (TideName[k] == lines[0]):
                        key1 = k
                    if (TideName[k] == lines[3]):
                        key2 = k

                hr[key1] = lines[1]
                pl[key1] = lines[2]
                hr[key2] = lines[4]
                pl[key2] = lines[5]
                line_num += 1
         
            else:
                exit

    fp.close()

    print("pt.name = %s" % name)
    print("pt.lat  = %s" % lat)
    print("pt.lon  = %s" % lon)
    print("pt.level= %s" % level)
            
    for i in range(60):
        print("pt.pl[%d]  = %6.2f    # %s" %(i,float(pl[i]),TideName[i]))

    for i in range(60):
        print("pt.hr[%d]  = %6.2f    # %s" %(i,float(hr[i]),TideName[i]))
