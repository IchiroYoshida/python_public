''''

  UVB_EDD.csv and daysDMil1.csv -> country,date(-7),date(+7) -> UVB

  2020-05-24

'''
import csv
import os

EDD_file = './data/csv/UVB_EDD.csv'
DM1_file = './data/csv/daysDMil1.csv'
DMil_file = './data/csv/DMil.csv'

dic_EDD = {}
dic_DM1 = {}
dic_DMil = {}

csvRow = []
#dic_EDD ---------------------------
EDD_csv =[]
with open(EDD_file) as f:
    reader = csv.reader(f)
    for row in reader:
        EDD_csv.append(row)

countries = EDD_csv[0]

del countries[:1]
del EDD_csv[:1]

for edd in EDD_csv:
    date = edd[0]
    del edd[:1]

    EDD_list = []
    for co in range(len(countries)):
        uvb = edd[co]
        country = countries[co]
        EDD_list.append([country, uvb])
    dic_EDD[date] = EDD_list
#dic_DM1 ---------------------------
DM1_csv =[]
with open(DM1_file) as f:
    reader = csv.reader(f)
    for row in reader:
        DM1_csv.append(row)
del DM1_csv[:1]

for dm1 in DM1_csv:
    country = dm1[0]
    date = dm1[1]
    td = dm1[2]
    dic_DM1[country] = [date, td]

#dic_DMil---------------------------
DMil_csv =[]
with open(DMil_file) as f:
    reader=csv.reader(f)
    for row in reader:
        DMil_csv.append(row)
del DMil_csv[:1]

for dmil in DMil_csv:
    country = dmil[0]
    Dmil = dmil[1]
    dic_DMil[country] = [Dmil]

countries =list(dic_DM1.keys())
dates = list(dic_EDD.keys())

for country in countries:
    dm1_data = dic_DM1[country]
    date = dm1_data[0]
    td = dm1_data[1]
    edd_data = dic_EDD[date]
    for edd in edd_data:
        country1 = edd[0]
        if (country == country1):
            day0 = dates.index(date)-7
            date14 = dates[day0:day0+14]

            n=0
            sum=0.
            for day in date14:
                edd_data2 = dic_EDD[day]
                for edd2 in edd_data2:
                    country2 = edd2[0]
                    uvb = edd2[1]
                    if (country == country2):
                        if (uvb is not 'NG'):
                            sum +=float(uvb)
                            n +=1
            val = sum/n
    try:
        Dmil = dic_DMil[country][0]
    except KeyError:
        Dmil = 'NG'
    csvRow.append([country,date,td,'{:5.3f}'.format(val),Dmil])

with open('./data/csv/EddRes.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country','Date(DMil>1.)','Td(7)','UVB EDD(J/m2)','DMil(200/05/20)'])
    writer.writerows(csvRow)

                        

