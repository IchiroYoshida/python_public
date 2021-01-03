'''
 SIR/Optuna model simulation

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
filename = './data/sir_optuna.res'

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
r0 = 2.5
I0 = 0.0         #Initial infected patients
beta = 0.0       # infection force 
gamma = beta /r0      # 1/duration

# Data to be fitted
dI_observed = X

def sir(v,t):
    global alpha, beta
    # v = [S, I, R]
    x = beta * v[0] * v[1]/N 
    y = gamma * v[1]
    dS = -x
    dI =  x - y
    dR =  y
    return np.array([dS, dI, dR])

def objective(trial):
    global alpha,beta, I0
    # パラメタ空間の定義
    beta  = trial.suggest_loguniform('beta', 1e-5,0.2) # infection force
    I0 = trial.suggest_uniform('I0', 0, 10000 )          # 初日感染者 0 - 1,0000人
    ini_state = [N-I0, I0, 0]   # 初期状態の感受性宿主数、感染者数、回復者数
    ode_int = odeint(sir, ini_state, tspan)  # 0日後 - tspan日後のS, I, Rを計算
    x = (ode_int[:,1])[1:]           # 1日後 - tspan日後の発症者数
    return mean_squared_error(x, dI_observed)  # 観測データとの2乗誤差

optuna.logging.disable_default_handler()
study = optuna.create_study()
study.optimize(objective, n_trials=100)
print("best_value = ", study.best_value)
print("best_params = ", study.best_params)
