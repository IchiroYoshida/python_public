import numpy as np
import ephem

def rnd2pi(x):
    return(x - np.floor(x /2*np.pi) * 2*np.pi)

obs = ephem.Observer()

obs.name = '福岡'
obs.lon = '130.390'
obs.lat = '33.593'
obs.date = '200000/08/18'
#obs.date ='2018/08/18'

