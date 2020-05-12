import csv
import requests
from bs4 import BeautifulSoup

col = 13
url="https://www.worldometers.info/coronavirus/"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table')

data = [dat.text for dat in table('td')]
csvRow = []


while len(data):
    row = data[:col]
    csvRow.append(row)
    del data[:col]

for line in csvRow:
    print(line[0])
