import countriesPos as pos
import os
import csv
import h5py
import numpy as np

def fname_date(fname):
    dates = fname.split('_')[2]
    yy = dates.split('m')[0]
    mmdd = dates.split('m')[1]

    mm = mmdd[:2]
    dd = mmdd[2:]

    date = yy+'/'+mm+'/'+dd
    return(date)

data_file_path = './nasa/Level3/'

Val = np.zeros((180, 360), dtype=float)
Tmp0 = np.zeros((180*360), dtype=float)
Tmp1 = np.zeros((180*360), dtype=float)

NUM = int(180*360)

countriesRow = ['']

countries = pos.countries.keys()

for country in countries:
    countriesRow.append(country)

files = os.listdir(data_file_path)
files.sort()

file = files[0]
fname = file.split('_v003')[0]

f = h5py.File(data_file_path+file,'r')
Tmp0 = np.array(f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/ErythemalDailyDose'][:][:].flatten())

csvRow = []

for f in range(len(files)-1):
    file = files[f+1]
    fname = file.split('_v003')[0]
    print('No.%d:'%(f+1),fname)

    f = h5py.File(data_file_path+file,'r')
    Tmp1 = np.array(f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/ErythemalDailyDose'][:][:].flatten())

    for i in range(NUM):
        val0 = Tmp0[i]
        val1 = Tmp1[i]
        if (val0 < 0):
            if (val1 > 0):
                Tmp1[i] = val1
        else:
            if (val1 > 0):
                Tmp1[i] = (val0 + val1)/2.
            else:
                Tmp1[i] = val0

    Tmp0 = Tmp1

    Val=np.reshape(Tmp1,(180,360))

    row=[fname_date(fname)]
    for country in countries:
        val =[]
        Lat = int(float(pos.countries[country][0]))+90
        Lon = int(float(pos.countries[country][1]))+180
        dat = float(Val[Lat, Lon])
        if (dat < 0):
            val ='NG'
        else:
            val = dat
        row.append(val)
    csvRow.append(row)

with open('./data/UVB_EDD.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(countriesRow)
    writer.writerows(csvRow)

