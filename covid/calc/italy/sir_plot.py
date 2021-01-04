'''
 SIR model simulation

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
r0 = 2.5
I0 = 816 
beta = 0.0599
gamma = beta /r0

def sir(v,t):
    global beta, gamma
    # v = [S, I, R]
    x = beta * v[0] * v[1]/N
    y = gamma * v[1]
    dS = -x
    dI =  x -y
    dR =  y
    return np.array([dS, dI, dR])

#Plot

ini_state = [N-I0,I0,0]

rcParams['figure.figsize'] = 12,7
ode_int = odeint(sir, ini_state, tspan)
plt.plot(ode_int)
plt.legend(['Susceptible','Infected','Recovered'])
plt.xlabel('Days')
plt.ylabel('Number of S/I/R patients')
plt.show()

