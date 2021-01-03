import os
 def getdirs(path):
     dirs=[]
     for item in os.listdir(path):
         if os.path.isdir(os.path.join(path,item)):
             dirs.append(item)
     return dirs

 path="/home/zope"       
 for dir in getdirs(path):
     print dir
