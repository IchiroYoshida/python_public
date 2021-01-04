'''
    Person method with SIR(U) model

    2020-07-04 Ichiro Yoshida
'''
Mesh = 25    # Mesh x Mesh grid 20
T  = 120      # Observation period days.100
N  = 1000     # Population 1000
I0 = 1      # Initial number of infected person

It = 7      # Infectious period of days
R0 = 2.73   # Reproduction number 
alpha = R0 /It
unsus = 40  # Unsusceptible population (%)

Xcenter = int(Mesh/2)
Ycenter = int(Mesh/2)

import numpy as np
import matplotlib.pylab as plt
import func.person2 as pn

#main

person = (N+1)*[]

inf = pn.Infection(person, Mesh, N, I0, It, alpha, unsus, Xcenter, Ycenter)
inf.initPerson()
inf.initInfection()

for t in range(T):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    print('No %d'%(t))
    pn.plotCell(inf,ax)
    fname = ('./out2/SIR%04d.png'%(t))
    title = ('%d day'%(t))
    plt.title(title)
    plt.savefig(fname)
    plt.close()

    inf.exposeInfection()
    inf.movePerson()
    inf.dailyReport()
