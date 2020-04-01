import math

t = 7.0
q0=[117,101,68,64,32,37,12,23,604]
q1=[153,123,105,100,69,52,32,31,892]

for i in range(9):
    Td = t *math.log(2)/math.log(q1[i]/q0[i])
    #m  = math.log(q1[i])/(t*math.log(q0[i]))
    m = ((q1[i]-q0[i])/t)/q1[i]
    print (Td,m)

