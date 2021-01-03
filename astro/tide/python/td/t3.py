#

import os

def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in fild_all_files('/Users/ichiro3/git/test0126/tide/python/td/TD2/'):
    print (file)
    try:
        fp = open(file,'r')
    except IOError as e:
        print('Cannot open %s ERR:' % file,e.errno)

    else:
        for line in fp:
            print(line,)

        fp.close()
