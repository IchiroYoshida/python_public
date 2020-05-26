import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

#Parameters
N=1000
t_max = 100
tspan =np.linspace(0.0, t_max,t_max+1)

I0 = 1  
R0 = 2.73
gamma = 1/7. 
beta  = R0*gamma /N

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

ode_I = ode_int[:,1]

plt.plot(ode_I)
plt.legend(['Infected'])
plt.xlabel('Days')
plt.ylabel('Number of Infected patients')
plt.show()
