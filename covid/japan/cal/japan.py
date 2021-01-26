'''
  JSONデータの読み込み

  2020-03-26 Ichiro Yoshida
'''
import json
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from pytz import timezone

url='https://www.stopcovid19.jp/data/covid19japan.json'

now= datetime.datetime.now()
filename= './jdata/area'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
now_jst = now.strftime('%Y/%m/%d %H:%M:%S JST')

s = requests.Session()
r = s.get(url)
json_data = json.loads(r.text)
area= (json_data['area'])

csvRow = []

for n in area:
    row=[n['name_jp'],n['npatients'],n['ndeaths']]
    csvRow.append(row)

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([now_jst])
    writer.writerows(csvRow)

