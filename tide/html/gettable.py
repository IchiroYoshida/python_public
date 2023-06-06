# 気象庁　潮位掲載地点一覧表の読み込み Ver 2.0
# 2023-06-05 Ichiro Yoshida
year = '2017'

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://www.data.jma.go.jp/kaiyou/db/tide/suisan/station'+year+'.php'
#station2011 - station2023
points_html = requests.get(url)
points = BeautifulSoup(points_html.content, 'html.parser')
table = points.find('table')
print(url)

datas = []
for tr in table.find_all('tr'):
    datas.append([td.text.strip() for td in tr.find_all('td')])

cols=['番号','地点記号','掲載地点名','緯度','経度','MSL潮位表基準面','MSL標高','潮位表基準面標高','M2振幅','M2遅角','S2振幅','S2遅角','K1振幅','K1角度','O1振幅','O1遅角','分潮一覧表','備考']

df = pd.DataFrame(datas[3:-1],columns=cols)
filename = './'+year+'/'+year+'.csv'
df.to_csv(filename, index=False)
