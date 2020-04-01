'''
    Person method with SIR model

    2020-03-30 Ichiro Yoshida
'''
Mesh = 3    # Mesh x Mesh grid
T  = 100      # Observation period days.
N  = 10     # Population
I0 = 1      # Initial number of infected person

It = 10        # Infectious period of days
alpha = 0.5    # Infectious force

Limit = Mesh -1

import numpy as np
import random

class Person:
    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.condition = 0 #[S, I, R]
        self.days = 0 #Duration from infection.

class Infection(object):
    def __init__(self,object, Mesh,N,IO,It,alpha):
        self.Mesh = Mesh
        self.person = (N+1)*[]
        self.N  = N
        self.I0 = I0
        self.It = It
        self.alpha = alpha
        self.Cell= [[[]*2 for i in range(Mesh)] for j in range(Mesh)]

        for n in range(0, self.N):
            self.person.append(Person())

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
        self.person[i].x = random.randrange(self.Mesh) 
        self.person[i].y = random.randrange(self.Mesh)
        self.person[i].condition = 0
        self.person[i].days = 0

    def initPerson(self):
        for i in range(0,N):
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

    def movePerson(self):
        for i in range(0,N):
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

person = (N+1)*[]

inf  = Infection(person, Mesh, N, I0, It, alpha)
inf.initPerson()
inf.initInfection()

for t in range(T):
    print('Day = ',t)
    for x in range(Mesh):
        for y in range(Mesh):
            member = inf.SIRinCell(x,y)
            s = member[0]
            i = member[1]
            r = member[2]
            print(' Cell[%d:%d] = S %10s I %10s R %10s' % (x,y,s,i,r))

    inf.exposeInfection()
    inf.movePerson()
    member = inf.dailyReport()
    print('Daily Report  %s '% member)

