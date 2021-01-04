import csv
import datetime
from pytz import timezone
import requests
from bs4 import BeautifulSoup

file_out = 'worldPop.csv'

col = 15
url="https://www.worldometers.info/coronavirus/"

now = datetime.datetime.now(timezone('UTC'))
filename = './mil/mil'+now.strftime('%Y%m%d_%H%M%S')+'.csv'
now_utc = now.strftime('%Y/%m/%d %H:%M:%S UTC')

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table')

data = [dat.text for dat in table('td')]
csvRow = []

while len(data):
    row = data[:col]
    country = row[1]
    pop  = row[13].replace(',','')
    csvRow.append([country,pop])
    del data[:col]

csvRow.sort(key=lambda x:str(x[0]))

del csvRow[:7]

with open(file_out,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country','Population'])
    writer.writerows(csvRow)
