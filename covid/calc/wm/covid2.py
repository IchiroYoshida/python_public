import csv
import datetime
from pytz import timezone
import requests
from bs4 import BeautifulSoup

col = 19 
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
    tot_Case = float(row[2].replace(',',''))
    if (len(row[4])>1):
        tot_Death = float(row[4].replace(',',''))
        if len(row[9]):
            case_Mil = float(row[9].replace(',',''))
            death_Mil = '{:.3f}'.format(tot_Death * case_Mil /tot_Case)
            csvRow.append([country, death_Mil])
    del data[:col]

csvRow.sort(key=lambda x: float(x[1]), reverse=True )
print(now_utc)

with open(filename,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country','Deaths/Mil.',now_utc])
    writer.writerows(csvRow)

