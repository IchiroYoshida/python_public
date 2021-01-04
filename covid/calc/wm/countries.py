import csv
import requests
from bs4 import BeautifulSoup

col = 15
url="https://www.worldometers.info/coronavirus/"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table')

data = [dat.text for dat in table('td')]
csvRow = []
csvRow2 = []

while len(data):
    row = data[:col]
    csvRow.append(row)
    del data[:col]

for line in csvRow:
    csvRow2.append([line[1],line[14]])

with open('country2.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csvRow2)

