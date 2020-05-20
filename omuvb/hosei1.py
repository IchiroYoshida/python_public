import numpy as np

a = np.zeros((5,3,3),dtype=float)
b = np.zeros((2,9),dtype=float)
res = np.zeros((3,3),dtype=float)

a[0]=np.array([[2,5,6],[-1,7,8],[3,-1,2]])
a[1]=np.array([[6,9,4],[3,-1,7],[2,-1,5]])
a[2]=np.array([[3,-1,8],[4,5,7],[1,2,9]])
a[3]=np.array([[2,3,-1],[7,1,-1],[2,6,5]])
a[4]=np.array([[3,8,2],[-1,-1,2],[4,8,9]])

b[0] = a[0].flatten()

print('init =',b[0])

for j in range(4):
    print('start %d'%(j),b[0])

    b[1]=a[j+1].flatten()
    print(j,b[1])

    for i in range(9):
        val0 = b[0][i]
        val1 = b[1][i]

        if(val0 < 0):
            if(val1 > 0):
                b[1][i] = val1
        else:
            if(val1 > 0):
                b[1][i]  = (val0 + val1)/2.
            else :
                b[1][i] = val0

    b[0] = b[1]

res = np.reshape(b[1],(3,3))
print('End=',res)



