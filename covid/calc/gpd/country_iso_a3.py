import csv
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

csvRow = []

names = world['name']
iso_a3 = world['iso_a3']

for t in range(len(names)):
    csvRow.append([names[t],iso_a3[t]])

csvRow.sort(key=lambda x: x[0])

with open('./name_iso_a3.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csvRow)

