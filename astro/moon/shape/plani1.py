import matplotlib.pyplot as plt
import numpy as np
import math

th = math.radians(30.)

x = np.linspace(0,350,36)
y = np.linspace(-90,80,36)

rad_x = np.radians(x)
rad_y = np.radians(y)

X,Y = np.meshgrid(rad_x,rad_y)

#plt.scatter(X,Y)
#plt.show()

h = math.sin(th)*np.sin(X) + math.cos(th)*np.cos(X)*np.cos(Y)
H = np.arcsin(h)

#if (np.all(np.cos(H) != 0)):
a = (math.cos(th)*np.sin(X) - math.sin(th)*np.cos(X)*np.cos(Y))/np.cos(H)
A = np.arccos(a)

plt.scatter(A,H)
plt.show()

"""
#print(A.shape,H.shape)
print(H)

H_new = H[np.where(H>0)]

print(H_new.shape)
print(H_new)
plt.scatter(A,H_new)
plt.show()

#condition = H > 0.
#H = np.extract(condition, H)

#new_H = np.any(i for i in H if i>0.)
#print(new_H)

#for i in H[:]:
#    if i < 0 : H.remove(i)

#for i in H:
#    if np.any(H >0) : new_H = H

#new_H = [ i for i in H if i >0.]
#print(new_H)

H2 = H.tolist()
A2 = A.tolist()

H_new = []
A_new = []

H_show = []
A_show = []

for i in H2:
    for j in i:
       H_new.append(j)

for i in A2:
    for j in i:
       A_new.append(j)

for i in H_new:
    if (i >0 ):
       H_show.append(i)
       A_show.append(A_new[i])

print(len(H_show),len(A_show))

for i in H2:
    for j in A2:
        if (i > 0) :
            H_new.append(i)
            A_new.append(j)

print (len(H_new),len(A_new))


for i in new_H:
    for j in new_A:
        print(i,j)
        
#print(new_H.shape,new_A)


#plt.scatter(new_A,new_H)
#plt.show()
"""

