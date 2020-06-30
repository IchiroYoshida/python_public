'''
  日本全国全体 JSON -> pike

  2020-06-30 Ichiro Yoshida
'''
import numpy as np
import json
import datetime
from pytz import timezone
import requests
import pandas as pd

url='https://www.stopcovid19.jp/data/covid19japan-all.json'
now=datetime.datetime.now()
pic_dir = './data/dst/jall'
now_jst = now.strftime('%Y%m%d_%H%M%S')
pic_file = pic_dir+now_jst+'.zip'

#get json file from URL
s = requests.Session()
r = s.get(url)

json_data = json.loads(r.text)

df = pd.json_normalize(json_data)
dates = df['lastUpdate']

print(len(dates))
'''
day = dates[0]
area = df['area']

df2 = pd.DataFrame(area[0])
df2.insert(0,'date',day)
df3 = df2.set_index(['date','name','name_jp'])
dd = df3.copy()

for d in range(1,len(dates)):
    df2 = pd.DataFrame(area[d])
    df2.insert(0,'date',day)
    df3 = df2.set_index(['date','name','name_jp'])
    dd = pd.concat([dd,df3], axis=0)

print(pic_file)
dd.to_pickle(pic_file)
'''

