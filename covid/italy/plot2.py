'''
   plot Italy

   2020-03-28
'''
import math
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

N = 60480000 
T = 50 # days

r0 = 2.73 #Reproduction number
beta = 0.297 # infection force
I0 = 1287
gamma = 0.154 # average rate or death(Hubei)
sigma = 1/7   # incubation average (7.0 days)

tspan = np.linspace(0.0, T, T+1)

read_csv = './data/Italy.csv'

def seir(v,t):
    global r0, beta, sigma, gamma
    # v = [S, E, I, R]
    x = beta*v[0]*v[2]/N # infected rate of the day
    dS = -x              # Susceptible
    dE = x - sigma * v[1] #Exposed
    dI = sigma * v[1] - gamma * v[2]   #Infected
    dR = gamma * v[1]    # Removed
    dN = dI +dR
    return np.array([dS, dE, dI, dR, dN])

csvRow = []

with open(read_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        csvRow.append([row][0])
del csvRow[:2]

C = []

for dat in csvRow:
    date = dat[0]
    cases = dat[1]
    deaths = dat[2]
    C.append(int(cases))

ini_state = [N-I0, I0, 0, 0, 0]
ode_int = odeint(seir, ini_state, tspan)

N = []
for t in range(len(ode_int)):
    ode = ode_int[t]
    N.append(int(ode[4]))

X = range(T)

for n in range(len(C)):
    plt.scatter(X[n],C[n],s=10,c="pink", linewidth="2", edgecolors="red")

for n in range(T):
    plt.scatter(X[n],N[n],s=10, c="blue", linewidth="2", edgecolors="blue")

plt.legend(['Cases in Italy'])
plt.xlabel('Days')
plt.ylabel('Cases with Simulation')
#plt.yscale('log')
plt.grid(which="both")
plt.show()
