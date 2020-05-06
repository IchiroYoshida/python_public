'''
  JSONデータから各国のCSVファイルへ

  2020-05-06 Ichiro Yoshida
'''
import json
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from pytz import timezone

url='https://pomber.github.io/covid19/timeseries.json'

now= datetime.datetime.now(timezone('UTC'))
now_utc = now.strftime('%Y/%m/%d %H:%M:%S UTC')

s = requests.Session()
r = s.get(url)
json_data = json.loads(r.text)
countries = json_data.keys()

for country in countries:
    csvRow=[]
    filename='./data/csv/'+country+'.csv'
    data = json_data[country]
    for n in data:
        row=[n['date'],n['confirmed'],n['deaths'],n['recovered']]
        csvRow.append(row)

    with open(filename,'w',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([now_utc])
        writer.writerows(csvRow)
