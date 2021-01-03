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

read_csv = './data/Italy.csv'
filename = './data/sird_optuna.res'

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
r0 = 2.6          #Basic reproduction number (1.5 - 3.0)
alpha = 0.0       # 感染率
beta = alpha/r0   # 回復率
fatalityrate= 0.0 # 死亡率
I0 = 0            # Init Infected patients

# Data to be fitted
dI_observed = X

def sird(v,t):
    global r0, alpha, beta,fatalityrate
    # v = [S, I, R, D]
    x = alpha *v[0] *v[2] / N   # infected rate of the day
    y = beta  * v[2] 
    dS = -x         # S:Susceptible
    dI =  x - y     # I:Infected
    dR = y          # R:Recovered or Dead
    dD = fatalityrate * y
    return np.array([dS, dI, dR, dD])

def objective(trial):
    global  alpha, beta, fatalityrate,I0
    # パラメタ空間の定義
    alpha = trial.suggest_uniform('alpha',0.,1.) # 感染率
    fatalityrate = trial.suggest_uniform('fatalityrate',0.,0.1) # 死亡率
    I0 = trial.suggest_uniform('I0', 0, 10000 )  # initial intected people
    ini_state = [N-I0, I0, 0, 0]   # Initialstate
    ode_int = odeint(sird, ini_state, tspan)  # 0日後 - tspan日後のS, I, Rを計算
    x = (beta * ode_int[:,1])[1:]           # 1日後 - tspan日後の発症者数
    return mean_squared_error(x, dI_observed)  # 観測データとの2乗誤差

optuna.logging.disable_default_handler()
study = optuna.create_study()
study.optimize(objective, n_trials=100)
print("best_value = ", study.best_value)
print("best_params = ", study.best_params)
