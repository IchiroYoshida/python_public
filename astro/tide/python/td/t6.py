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

            line_num=0
            
            tn=[""]*40
            pl=[0]*40
            hr=[0]*40
            
            try:
                fp = open(file_td2,'r')
                fp40 = open(file_td40,'w')

            except IOError as e:
                print('Cannot open %s ERR:' % file_td2,e.errno)

            else:
                for line in fp:
                   line=line.replace(" ","")
                   line=line.replace("\n","")
                   line=line.replace("\x1a","")
                   lines=line.split(",")

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
                   
                   #fp40.write(line,)
                   
            fp.close()
            
            print("pt.name = %s" % name)
            print("pt.lat  = %s" % lat)
            print("pt.level= %s" % level)
            

            for i in range(40):
                print("pt.pl[%d]  = %s    # %s " %(i,pl[i],tn[i]))

            for i in range(40):
                print("pt.hr[%d]  = %s    # %s " %(i,hr[i],tn[i]))

            fp40.close()

