import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

#Parameters
N=3711
t_max = 100
tspan =np.linspace(0.0, t_max,t_max+1)

alpha = 0.099
I0 =302.3
beta = 4.676e-5
gamma = 0.148

def sir(v,t):
    global alpha,beta,gamma
    # v = [S, I, R]
    x = beta*v[0]*v[2]
    dS = -x
    dR = gamma * v[1]
    dI = x - dR
    return np.array([dS, dI, dR])

ini_state = [N-I0,I0,0]

rcParams['figure.figsize']=12,7
ode_int = odeint(sir, ini_state, tspan)
plt.plot(ode_int)
plt.legend(['Susceptible','Infected','Recovered'])
plt.xlabel('Days')
plt.ylabel('Number of S/I/R patients')
plt.show()


