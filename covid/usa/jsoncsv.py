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

url='https://coronavirus-tracker-api.herokuapp.com/all'

now= datetime.datetime.now(timezone('UTC'))
now_utc = now.strftime('%Y/%m/%d %H:%M:%S UTC')

s = requests.Session()
r = s.get(url)
json_data = json.loads(r.text)
keys = json_data.keys()

data1 = json_data['confirmed']
data2 = data1['locations']

for dat2 in data2:
    keys = dat2.keys()
    country = dat2['country']
    province = dat2['province']
    coordinates = dat2['coordinates']
    lat = coordinates['lat']
    long = coordinates['long']
    print(country, province, lat, long)

'''
for key in keys:
    data1 = json_data[key]
    keys2 = data1.keys()
    for key2 in keys2:
        csvRow=[]
        data2 = data1[key2]
        for d in data2:
             if(type(d) is list):
                 row=[d['country'],d['country_code'],d['province'],d['coordinates'],d['history'],d['latest']]
                 csvRow.append(row)
             else:
                 print(key,key2,d)

        print(key,key2,csvRow)

    for n in data:
        row=[n['date'],n['confirmed'],n['deaths'],n['recovered']]
        csvRow.append(row)

    with open(filename,'w',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([now_utc])
        writer.writerows(csvRow)
'''
