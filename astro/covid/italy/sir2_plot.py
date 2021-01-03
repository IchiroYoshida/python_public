'''
 SIR model simulation

 '''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

N = 60480000          # community size
t_max = 600 
tspan = np.linspace(0.0, t_max, t_max + 1)

# parameters to fit
alpha = 0.0878       # 感染者の発症率 
I0 = 4752            # Init Infected patients
beta = 0.00196       # infection force
gamma = 0.0832       # 14日で感染力がなくなる
fatalityrate = 0.032        # 死亡率

def sir2(v,t):
    global alpha, beta, gamma, fatalityrate
    # v = [S, R, D, I]
    x = beta*v[0]*v[2]/N   # その日の新たな感染者数
    dS = -x              # 感受性宿主の差分
    dR = gamma * v[1]    # 感染者の中でその日に回復する数（回復者数の差分）
    dD = fatalityrate * v[1] # 感染者の中でその日に死亡する数
    dI = x - dR -dD         # 感染者数の増減
    return np.array([dS, dR, dD, dI])

#Plot

ini_state = [N-I0,I0,0, 0]

rcParams['figure.figsize'] = 12,7
ode_int = odeint(sir2, ini_state, tspan)
plt.plot(ode_int)
plt.legend(['Susceptible','Infected','Recovered'])
plt.xlabel('Days')
plt.ylabel('Number of S/I/R patients')
plt.show()

