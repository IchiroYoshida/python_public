'''
  日本全国全体 JSON -> pike

  2020-07-23 Ichiro Yoshida
'''
import numpy as np
import json
import datetime
from pytz import timezone
import requests
import pandas as pd

def filtnan(df):
    col =['npatients','ncurrentpatients','nexits','ndeaths']
    for c in col:
        dats = df[c]
        dat = dats.values.tolist()
        dlist = []
        for da in dat:
            if (da == '-'):
               da = np.nan
            if (da == '不明'):
               da = np.nan
            dlist.append(da)
        df[c] = dlist
    return(df)

url='https://www.stopcovid19.jp/data/covid19japan-all.json'
now=datetime.datetime.now()
pic_dir = './data/json/jall'
now_jst = now.strftime('%Y%m%d_%H%M%S')
pic_file = pic_dir+now_jst+'.zip'

#get json file from URL
s = requests.Session()
r = s.get(url)

json_data = json.loads(r.text)

df = pd.json_normalize(json_data)
dates = df['lastUpdate']
area = df['area']

day = dates[0]
df2 = pd.DataFrame(area[0])

df3 = filtnan(df2)
sum3 = df3.sum()
sum_npatients = sum3['npatients']
sum_ncurrentpatients = sum3['ncurrentpatients']
sum_nexits = sum3['nexits']
sum_ndeaths = sum3['ndeaths']

df4 = df3.append({'name': 'Zenkoku',
        'name_jp': '全国',
        'npatients': sum_npatients,
        'ncurrentpatients': sum_ncurrentpatients,
        'nexits': sum_nexits,
        'ndeaths': sum_ndeaths},ignore_index=True)

df4.insert(0,'date',day)
df5 = df4.set_index(['date','name','name_jp'])
dd = df5.copy()

for d in range(1,len(dates)):
    day = dates[d]
    df2 = pd.DataFrame(area[d])
    df3 = filtnan(df2)
    sum3 = df3.sum()
    sum_npatients = sum3['npatients']
    sum_ncurrentpatients = sum3['ncurrentpatients']
    sum_nexits = sum3['nexits']
    sum_ndeaths = sum3['ndeaths']
    df4 = df3.append({'name': 'Zenkoku',
            'name_jp': '全国',
            'npatients': sum_npatients,
            'ncurrentpatients': sum_ncurrentpatients,
            'nexits': sum_nexits,
            'ndeaths': sum_ndeaths},ignore_index=True)

    df4.insert(0,'date',day)
    df5 = df4.set_index(['date','name','name_jp'])
    dd = pd.concat([dd,df5], axis=0)

print(pic_file)
dd.to_pickle(pic_file)

