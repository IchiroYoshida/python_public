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
r0 = 2.73  #Reproduction number
beta = 0.297 # infection force
I0 = 1287            # Init Infected patients
gamma = 0.154 # average rate or death (Hubei)
sigma = 1/7 # incubation average (7.0 days)
fatalityrate = 0.03

def seir(v,t):
    global r0, beta, sigma, gamma, Sum
    # v = [S, E, I, R, Sum]
    x = beta*v[0]*v[2]/N # infected rate of the day
    dS = -x              # Susceptible
    dE = x - sigma * v[1] #Exposed
    dI = sigma * v[1] - gamma * v[2]   #Infected
    dR = gamma * v[2]    # Removed
    dN = (dI + dR) * fatalityrate 
    return np.array([dS, dE, dI, dR, dN])

#Plot

ini_state = [N-I0,I0,0, 0,0]

rcParams['figure.figsize'] = 12,7
ode_int = odeint(seir, ini_state, tspan)
plt.plot(ode_int)
plt.legend(['Susceptible','Exposed','Infected','Recovered','Total deaths'])
plt.xlabel('Days')
plt.ylabel('Number of S/E/I/R Total.patients')
plt.show()

