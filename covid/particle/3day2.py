'''
    Person method with SIR model

    2020-04-01 Ichiro Yoshida
'''
Mesh = 50    # Mesh x Mesh grid
T  = 100      # Observation period days.
N  = 10000     # Population
I0 = 1      # Initial number of infected person

It = 7      # Infectious period of days
R0 = 2.208   # Reproduction number 
alpha = R0 /It

Limit = Mesh -1

import numpy as np
import random
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

class Person:
    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.condition = 0 #[S, I, R]
        self.days = 0 #Duration from infection.

class Infection(object):
    def __init__(self,object, Mesh,N,IO,It,alpha):
        self.person = (N+1)*[]
        self.Cell= [[[]*2 for i in range(Mesh)] for j in range(Mesh)]
        [self.person.append(Person()) for n in range(N)]

    def cellAppend(self, object):
        i  = object.id
        xx = object.x
        yy = object.y
        self.Cell[xx][yy].append(i)

    def cellRemove(self, object):
        i  = object.id
        xx = object.x
        yy = object.y
        self.Cell[xx][yy].remove(i)

    def resetPerson(self, i):
        self.person[i].id = i
        self.person[i].x = random.randrange(Mesh) 
        self.person[i].y = random.randrange(Mesh)
        self.person[i].condition = 0
        self.person[i].days = 0

    def initPerson(self):
        for i in range(N):
            self.resetPerson(i)
            xx = self.person[i].x
            yy = self.person[i].y
            self.cellAppend(self.person[i])

    def initInfection(self):
        members = self.person
        infected = random.sample(members,I0)

        for inf in infected:
            id = inf.id
            self.person[id].condition = 1
            self.person[id].days = It

    def removeCheck(self):
        for n in range(N):
            dy = self.person[n].days
            if (dy > (It - 3)):
                if(random.random() > ( 1 - .2 )):
                    self.person[n].condition = 2   # R: Recoved
            
            
    def movePerson(self):
        for i in range(N):
            self.cellRemove(self.person[i])

            xx = self.person[i].x
            yy = self.person[i].y

            vx = random.randrange(3) - 1
            vy = random.randrange(3) - 1

            xx = xx + vx
            yy = yy + vy

            if (xx > Limit):
                xx = Limit
            if (yy > Limit):
                yy = Limit
            if (xx < 0):
                xx = 0
            if (yy < 0):
                yy = 0

            self.person[i].x = xx
            self.person[i].y = yy
            
            self.cellAppend(self.person[i])

    def SIRinCell(self,x,y):
        member = self.Cell[x][y]
        s,i,r  = [],[],[]
        for m in member:
            condition = self.person[m].condition
            if (condition == 0):
                s.append(m)
            if (condition == 1):
                i.append(m)
            if (condition == 2):
                r.append(m)
        return([s,i,r])

    def exposeInfection(self):
        for x in range(Mesh):
            for y in range(Mesh):
                member = self.SIRinCell(x,y)
                s = member[0]
                i = member[1]
                r = member[2]
                for ii in i:
                    for ss in s:
                        if (random.random() > (1. - alpha)): #Infect!!
                            self.person[ss].condition = 1
                            self.person[ss].days = It

    def dailyReport(self):
        s, i, r = [],[],[]
        for n in range(N):
            if(self.person[n].condition == 0): # Susceptible
                s.append(n)

            elif(self.person[n].condition == 1): # Infected
                i.append(n)

                if (self.person[n].days):
                    self.person[n].days -= 1
                else:
                    self.person[n].condition = 2 #Recovered
                    r.append(n)
            else :  
                r.append(n)

        return([s, i, r])


#main

x = np.arange(0, T, 1)
i1,i2 = [], []

person1 = (N+1)*[]

inf1  = Infection(person1, Mesh, N, I0, It, alpha)
inf1.initPerson()
inf1.initInfection()

for t in range(T):
    member = inf1.dailyReport()
    i1.append(len(member[1]))
    inf1.exposeInfection()
    inf1.removeCheck()
    inf1.movePerson()

I1 = np.array(i1)

person2 = (N+1)*[]

inf2 = Infection(person2, Mesh, N, I0, It, alpha)
inf2.initPerson()
inf2.initInfection()

for t in range(T):
    member = inf2.dailyReport()
    i2.append(len(member[1]))
    inf2.exposeInfection()
    inf2.movePerson()

I2 = np.array(i2)

plt.plot(I1)
plt.plot(I2)

plt.legend(['Removed within 3days','not Removed'])
plt.xlabel('Days')
plt.ylabel('Number of infected patients')
plt.show()
