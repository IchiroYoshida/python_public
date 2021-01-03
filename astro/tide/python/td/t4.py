#

import os

DIR = '/Users/ichiro3/git/test0126/tide/python/td/TD2/TEST/'

def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in fild_all_files(DIR):
    file_name = file.rsplit("/",1)
    file_name_TD2 = file_name[1].split(".")
    if len(file_name_TD2) > 1:
        if (file_name_TD2[1]=="TD2"):
            file_td2=DIR+file_name_TD2[0]+".TD2"
            file_td40=DIR+file_name_TD2[0]+".td40"

            try:
                fp = open(file_td2,'r')
                fp40 = open(file_td40,'w')

            except IOError as e:
                print('Cannot open %s ERR:' % file_td2,e.errno)

            else:
                for line in fp:
                   lines=line.split(",")
                   print(lines)

                fp40.write(line,)
            fp.close()
            fp40.close()

