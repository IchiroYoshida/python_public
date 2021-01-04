'''
 SEIR model plotting

 2020-03-28
'''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

N = 60480000          # community size
t_max = 300 
tspan = np.linspace(0.0, t_max, t_max + 1)

# parameters to fit
r0 = 2.67  #Reproduction number
beta = 0.205 # infection force
I0 = 7123           # Init Infected patients
gamma = 0.154 # average rate or death (Hubei)
sigma = 1/7 # incubation average (7.0 days)

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

ini_state = [N-I0,I0,0, 0,0]

#rcParams['figure.figsize'] = 12,7
ode_int = odeint(seir, ini_state, tspan)

for n in range(len(ode_int)):
    ode = ode_int[n]
    S = int(ode[0])
    E = int(ode[1])
    I = int(ode[2])
    R = int(ode[3])
    N = int(ode[4])
    print(n,N)

