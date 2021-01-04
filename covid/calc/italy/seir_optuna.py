'''
 SEIR/Optuna model simulation

 2020-03-28
'''

import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import optuna
plt.style.use('seaborn-colorblind')
import math
import csv
import datetime

read_csv = './data/Italy2.csv'
#filename = './data/seir_optuna.res'

csvRow = []
data = {}

with open(read_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        csvRow.append(row)

del csvRow[:2]
del csvRow[-1]

for lin in csvRow:
    date = lin[0].split('-')
    date_str = date[0]+date[1]+date[2]
    cases = int(lin[1])
    deaths = int(lin[2])

    data[date_str]=[date,cases,deaths]

days = list(data.keys())
ndays = len(days)

X=[]

for d in range(ndays-1):
    day0 = days[d]
    day1 = days[d+1]
    dx = data[day1][1]-data[day0][1]
    X.append(dx)

N = 60480000          # community size
t_max = len(X) 
tspan = np.linspace(0.0, t_max, t_max + 1)

# parameters to fit
r0 = 0.0          #Basic reproduction number (1.5 - 3.0)
beta = 0.0        #product of the people exposed to each day by infected people
sigma =  1/7      # incubation rate average 7.0 days
gamma = 0.154     # 1/gamma = average rate of recovery or death
I0 = 20            # Init Infected patients

# Data to be fitted
dI_observed = X

def seir(v,t):
    global r0, beta, sigma, gamma
    # v = [S, E, I, R]
    x = beta*v[0]*v[2]/N   # infected rate of the day
    dS = -x                # Susceptible
    dE = x - sigma * v[1]  # Exposed 
    dI = sigma * v[1] - gamma * v[2]  #Infected 
    dR = gamma * v[2]    # Removed
    return np.array([dS, dE, dI, dR])

def objective(trial):
    global r0, beta, I0
    # パラメタ空間の定義
    r0 = trial.suggest_uniform('r0', 1.5, 3.0)  #Reproduction number
    beta = trial.suggest_loguniform('beta', 0.1, 1.0) # infected rate by day
    #I0 = trial.suggest_uniform('I0', 0, 10000 )       # initial intected people
    ini_state = [N-I0, I0, 0, 0]   # Initialstate
    ode_int = odeint(seir, ini_state, tspan)  # 0日後 - tspan日後のS, I, Rを計算
    x = (ode_int[:,1])[1:]           # 1日後 - tspan日後の発症者数
    return mean_squared_error(x, dI_observed)  # 観測データとの2乗誤差

optuna.logging.disable_default_handler()
study = optuna.create_study()
study.optimize(objective, n_trials=100)
print("best_value = ", study.best_value)
print("best_params = ", study.best_params)


