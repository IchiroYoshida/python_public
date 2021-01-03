import csv
import datetime
from pytz import timezone
import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/"

now = datetime.datetime.now(timezone('UTC'))
filename = './csv/covid'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
now_utc = now.strftime('%Y/%m/%d %H:%M:%S UTC')

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table')

data = [dat.text for dat in table('td')]
csvRow = []

while len(data):
    row = data[:11]
    csvRow.append(row)
    del data[:11]

print(now_utc)
with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([now_utc])
    writer.writerows(csvRow)
