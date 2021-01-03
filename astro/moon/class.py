class MyClass(object):
   def __init__(self,name,x,y):
      self.name = name
      self.x    = x
      self.y    = y

dat=[]

dat.append(MyClass('No1 name',10,5))
dat.append(MyClass('No2 aho',3.14,2.18))

print (dat[0].name,dat[1].name)
