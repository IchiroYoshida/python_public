'''
 SIR model simulation

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
alpha = 0.0       # 感染者の発症率 
I0 = 0            # Init Infected patients
beta = 0.0        # infection force
gamma = 0.0       # 14日で感染力がなくなる

# Data to be fitted
dI_observed = X

def sir(v,t):
    global alpha, beta, gamma
    # v = [S, I, R]
    x = beta*v[0]*v[2]   # その日の新たな感染者数
    dS = -x              # 感受性宿主の差分
    dR = gamma * v[1]    # 感染者の中でその日に回復する数（回復者数の差分）
    dI = x - dR          # 感染者数の増減
    return np.array([dS, dI, dR])

def objective(trial):
    global beta,gamma,alpha,I0
    # パラメタ空間の定義
    alpha = trial.suggest_uniform('alpha', 0.001, 0.1)  # 1日あたり発症率 0.1% - 10%
    beta = trial.suggest_loguniform('beta', 1e-5, 1e-1) # 感染率 0.001% - 10%
    gamma = trial.suggest_uniform('gamma', 0.05, 0.1)   # 感染期間 2日 - 20日
    I0 = trial.suggest_uniform('I0', 0, 10000 )          # 初日感染者 0 - 1,0000人
    ini_state = [N-I0, I0, 0]   # 初期状態の感受性宿主数、感染者数、回復者数
    ode_int = odeint(sir, ini_state, tspan)  # 0日後 - tspan日後のS, I, Rを計算
    x = (alpha * ode_int[:,1])[1:]           # 1日後 - tspan日後の発症者数
    return mean_squared_error(x, dI_observed)  # 観測データとの2乗誤差

optuna.logging.disable_default_handler()
study = optuna.create_study()
study.optimize(objective, n_trials=100)
print("best_value = ", study.best_value)
print("best_params = ", study.best_params)

'''
#Plot

I0 = study.best_params['I0']
alpha = study.best_params['alpha']
beta = study.best_params['beta']
gamma = study.best_params['gamma']

ini_state = [N-I0,I0,0]

rcParams['figure.figsize'] = 12,7
ode_int = odeint(sir, ini_state, tspan)
plt.plot(ode_int)
plt.legend(['Susceptible','Infected','Recovered'])
plt.xlabel('Days')
plt.ylabel('Number of S/I/R patients')
plt.show()
'''


