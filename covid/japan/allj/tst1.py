import numpy as np
import pandas as pd

CSV = './data/pref_data.csv'

PrefDF =pd.read_csv(CSV, index_col =0)
#print(PrefDF)

prefs = PrefDF.index
prefs_list = prefs.values.tolist()
pref_pop = PrefDF['popNum']
pref_pop_list = pref_pop.values.tolist()

for pref in prefs_list:
    idx = prefs_list.index(pref)
    popNum = float(pref_pop_list[idx])/100000
    print(pref,popNum)
    