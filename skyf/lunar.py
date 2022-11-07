from skyfield.api import load
from skyfield import eclipselib
import pandas as pd
import numpy as np

ts = load.timescale()
t0 = ts.utc(2022, 1, 1)
t1 = ts.utc(2022,12,31)

eph = load('de421.bsp')

t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)

de = pd.DataFrame.from_dict(details).T
print(de)

print(t)

for ti, yi in zip(t, y):
    print(ti.utc_strftime('%Y-%m-%d %H:%M'),
        'y={}'.format(yi),
        eclipselib.LUNAR_ECLIPSES[yi])

