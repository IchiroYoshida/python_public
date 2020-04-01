'''
    Person method with SIR model
'''
#Mesh = 20    # Mesh x Mesh grid
#T  = 100      # Observation period days.
#N  = 1000     # Population
#I0 = 10      # Initial number of infected person

#It = 14      # Infectious period of days
#R0 = 2.0 
#alpha = R0 /It

#print('Limit',Limit)

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
    def __init__(self,object, Mesh, N, I0, It, alpha):
        self.Mesh = Mesh
        self.N = N
        self.I0 = I0
        self.It = It
        self.alpha = alpha
        self.person = (self.N+1)*[]
        self.Cell= [[[]*2 for i in range(self.Mesh)] for j in range(self.Mesh)]
        [self.person.append(Person()) for n in range(self.N)]

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
        infected = random.sample(members,self.I0)

        for inf in infected:
            id = inf.id
            self.person[id].condition = 1
            self.person[id].days = It

    def movePerson(self):
        for i in range(self.N):
            self.cellRemove(self.person[i])

            xx = self.person[i].x
            yy = self.person[i].y

            vx = random.randrange(3) - 1
            vy = random.randrange(3) - 1

            xx = xx + vx
            yy = yy + vy

            if (xx > self.Limit):
                xx = self.Limit
            if (yy > self.Limit):
                yy = self.Limit
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
        for x in range(self.Mesh):
            for y in range(self.Mesh):
                member = self.SIRinCell(x,y)
                s = member[0]
                i = member[1]
                r = member[2]
                for ii in i:
                    for ss in s:
                        if (random.random() > (1. - self.alpha)): #Infect!!
                            self.person[ss].condition = 1
                            self.person[ss].days = self.It


    def dailyReport(self):
        s, i, r = [],[],[]
        for n in range(self.N):
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


if __name__ == '__main__':

    person = (N+1)*[]

    inf  = Infection(person, Mesh, N, I0, It, alpha)
    inf.initPerson()
    inf.initInfection()

    for t in range(T):
        print('Day = ',t)
        member = inf.dailyReport()
        s = len(member[0])
        i = len(member[1])
        r = len(member[2])
        print('S={0} I={1} R={2}'.format(s,i,r))
        if not member[1]:
           break 
        inf.exposeInfection()
        inf.movePerson()
