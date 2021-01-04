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
t_max = 200 
tspan = np.linspace(0.0, t_max, t_max + 1)

# parameters to fit
alpha = 0.623       # 感染率
beta = 0.0505       # 回復率
fatalityrate= 0.03  # 死亡率
I0 = 9995            # Init Infected patients

def sird(v,t):
    global alpha, beta,fatalityrate
    # v = [S, I, R, D]
    x = alpha *v[0] *v[2] / N   # infected rate of the day
    y = beta  * v[1] 
    dS = -x         # S:Susceptible
    dI =  x - y     # I:Infected
    dR =  y         # R:Recovered or Dead
    dD = fatalityrate * y
    return np.array([dS, dI, dR, dD])

ini_state = [N-I0, I0, 0, 0]

ode_int = odeint(sird, ini_state, tspan)

num = len(ode_int)
for d in range(num):
    print(d,ode_int[d])
