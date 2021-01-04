'''
    Person method with SIR model

    2020-05-26 Ichiro Yoshida
'''
Repeat =  100    #1000 
Mesh = 25    # Mesh x Mesh grid 20
T  = 100      # Observation period days.100
N  = 1000     # Population 1000
I0 = 1      # Initial number of infected person

It = 7      # Infectious period of days
R0 = 2.73   # Reproduction number 
alpha = R0 /It
unsus = 50

Xcenter = int(Mesh/2)
Ycenter = int(Mesh/2)

import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')
import func.person2 as pn

#main

person = (N+1)*[]

inf  = pn.Infection(person, Mesh, N, I0, It, alpha, unsus, Xcenter, Ycenter)
inf.initPerson()
inf.initInfection()

x = np.arange(0, T, 1)

i = []
for t in range(T):
    inf.exposeInfection()
    inf.movePerson()
    member = inf.dailyReport()
    i.append(len(member[1]))

Inf0  = np.array(i)

print(0,Inf0)

# Step 1...Repeat
for rep in range(1,Repeat):
    print('No. %d'%(rep))
    person = (N+1)*[]

    inf  = pn.Infection(person, Mesh, N, I0, It, alpha, unsus, Xcenter, Ycenter)
    inf.initPerson()
    inf.initInfection()

    i = []
    for t in range(T):
        inf.exposeInfection()
        inf.movePerson()
        member = inf.dailyReport()
        i.append(len(member[1]))

    Inf1 = np.array(i)
    max = Inf1.max()
    if (max > 10):
        Inf0 = (Inf0+Inf1)/2. 
        plt.plot(Inf1,zorder=0)
        print(t,Inf1)
    
plt.plot(Inf0,color='red',linewidth =5. ,zorder=1)

plt.legend(['Infected'])
plt.xlabel('Days')
plt.xlim(0,100)
plt.ylim(0,500)
plt.ylabel('Number of Infected Total. patients')
plt.show()
plt.close()
