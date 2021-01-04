'''
https://nbviewer.jupyter.org/github/hayashiyus/COVID-19/blob/master/stochasticSEIRmodel.ipynb
'''


import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

#parameters
N = 60480000 #community size
E0 = 5000 #init Exposed patients
R0 = 2.2 
lp = 5.5 #latent period(days)
ip = 20 #infectious period(days)
beta = R0 / ip

#differential equation: SEIR model
def seir(v, t):
    dS = -beta*v[0]*v[2]
    dE = beta*v[0]*v[2] - (1/lp)*v[1]
    dI = (1/lp)*v[1] - (1/ip)*v[2]
    dR = (1/ip)*v[2]
    return np.array([dS, dE, dI, dR])

#solve SEIR model
              #S #E #I #R 
ini_state = [N-E0, E0, 0, 0]
t_max = 100
tspan = np.linspace(0.0, t_max, t_max)
rcParams['figure.figsize'] = 12, 7
plt.plot(odeint(seir, ini_state, tspan))
plt.legend(['Susceptible', 'Exposed', 'Infected', 'Recovered'])
plt.xlabel('Days')
plt.ylabel('Number of S/E/I/R patients')
plt.show()

import sdeint

#stochastic SEIR model
#Random force
def G(v, t):
    cor = np.array([[1, -1.5], [-3, 5], [3, -5], [-1, 1.5]])
    return np.cov(cor, rowvar=1, bias=1) 

rcParams['figure.figsize'] = 12, 7
plt.plot(sdeint.itoint(seir, G, ini_state, tspan))
plt.legend(['Susceptible', 'Exposed', 'Infected', 'Recovered'])
plt.xlabel('Days')
plt.ylabel('Number of S/E/I/R patients')
plt.show()

