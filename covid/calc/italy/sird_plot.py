'''
 SIRD/Optuna1 model simulation Plot

 2020-03-28
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

N = 60480000          # community size
t_max = 365 
tspan = np.linspace(0.0, t_max, t_max + 1)

# parameters to fit
r0 = 2.2 
beta = 0.074
gamma = beta /r0
fatalityrate= 0.085  # 死亡率
I0 = 484            # Init Infected patients

def sird(v,t):
    global alpha, beta,fatalityrate
    # v = [S, I, R, D]
    x = beta *v[0] *v[1] / N   # infected rate of the day
    y = gamma  * v[1] 
    dS = -x         # S:Susceptible
    dI =  x - y     # I:Infected
    dR =  y         # R:Recovered or Dead
    dD = fatalityrate * y
    dN = dI + dR
    return np.array([dS, dI, dR, dD, dN])

#Plot

ini_state = [N-I0, I0, 0, 0, 0]

rcParams['figure.figsize'] = 12, 7
ode_int = odeint(sird, ini_state, tspan)
plt.plot(ode_int)
plt.legend(['Susceptible','Infected','Recovered','Dead','Total Cases'])
plt.xlabel('Days')
plt.ylabel('Number of S/I/R/D populations')
plt.show()

