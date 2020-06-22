'''
JSON Data -> pickle file(.zip) (Pandas)

2020-06-22 Ichiro Yoshida
'''
import numpy as np
import json
import datetime
from pytz import timezone
import requests
import pandas as pd

url='https://pomber.github.io/covid19/timeseries.json'

now= datetime.datetime.now(timezone('UTC'))
now_utc = now.strftime('%Y%m%d_%H%M%S')

#----- get pomber(GitHub) countries data ----------
s = requests.Session()
r = s.get(url)

json_data = json.loads(r.text)

df = pd.json_normalize(json_data)

pic_file = './data/pomber/pom_'+now_utc+'.zip'
print(pic_file)
df.to_pickle(pic_file)
