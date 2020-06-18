'''
Pickle Data -> countries.csv (Pandas)

2020-06-16 Ichiro Yoshida
'''
import datetime
import os
import pandas as pd

Index=['date', 'confirmed', 'deaths', 'recovered',
       'Cases Total(Ave7)', 'Cases Day', 'Cases Day(Ave7)',
       'Deaths Total(Ave7)', 'Deaths Day', 'Deaths Day(Ave7)',
       'Deaths Weekly(Ave7)/1M pop', 'Deaths /1M pop (Ave7)',
       'Td7', 'R0','K','CFR']

def str2date(d):
   tmp = datetime.datetime.strptime(d,'%Y-%m-%d')
   return datetime.date(tmp.year, tmp.month, tmp.day)

pic_path = './data/dst/'
csv2_path = './data/csv2/'

files = os.listdir(pic_path)
files.sort()

file = files[-1]

df = pd.read_pickle(pic_path+file)

df1 = df.set_index(["Country"])
df1.sort_index(inplace=True)
countries = list(set(list(df1.index)))
countries.sort()

for country in countries:
    c = df1.loc[country]
    c2 = c.values
    sort_c2 = sorted(c2, key=lambda x: str2date(str(x[0])))
    csv = pd.DataFrame(sort_c2,columns=Index)
    file_name = csv2_path+country+'.csv'
    print(file_name)
    csv.to_csv(file_name)

