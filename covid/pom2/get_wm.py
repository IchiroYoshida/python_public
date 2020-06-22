'''
Worldmeters corona virus Web Table -> pickle file(.zip) (Pandas)

2020-06-22 Ichiro Yoshida
'''
import math
import numpy as np
import datetime
from pytz import timezone
import requests
import pandas as pd
from bs4 import BeautifulSoup

df_col = 17

csv2_path = './data/csv2/'

wmc='https://www.worldometers.info/coronavirus/'

now= datetime.datetime.now(timezone('UTC'))
now_utc = now.strftime('%Y%m%d_%H%M%S')

#----- get worldmeter coronavirus countries data ---
# HTML table -> CSV

wm_res = requests.get(wmc)
wm_soup = BeautifulSoup(wm_res.text, 'html.parser')
wm_table = wm_soup.find('table')
wm_data = [dat.text for dat in wm_table('td')]
wm_col = 19   #colums of the worldmeters HTML table

csvRow = []

while len(wm_data):
    row = wm_data[:wm_col]
    del row[:1]
    del row[6]
    del row[-3:]
    csvRow.append(row)
    del wm_data[:wm_col]

del csvRow[:8]   # Delete Head.
del csvRow[-8:]  # Delete Tail.

new_col = 12
newlist = []
while len(csvRow):
    newRow = []
    row = csvRow[:wm_col][0]
    del row[2]
    del row[3]
    newRow.append(row[0])
    del csvRow[:1]
    for dd in range(1,new_col-1):
        new_dat = row[dd].replace(',','').replace(' ','')
        newRow.append(new_dat)
    newlist.append(newRow)

wmp = pd.DataFrame(newlist, columns=['Country','Total Cases','Total Deaths',\
    'Total Recovered','Active Cases','Serious Critical','Tot Cases/1M pop',\
    'Deaths/1M pop','Total Tests','Tests/1M pop','Population'])

pic_file = './data/wmp/wmp_'+now_utc+'.zip'
print(pic_file)
wmp.to_pickle(pic_file)
