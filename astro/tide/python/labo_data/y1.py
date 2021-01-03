import os
FILE = 'yonara.txt'

tide= []

try:
    fp = open(FILE,'r')

except IOError as e:
    print('Cannot open %s ERR:' % FILE,e.errno)

else:
    for line in fp:
        line1=line.replace('\n','')
        if (line1[0]!='#'):
            lines=line1.split(',')
            tide.extend(map(int,lines))

print (tide)

