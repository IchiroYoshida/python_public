import countriesPos as pos
import csv
import h5py
import numpy as np

data_file_path = './nasa/Level3/'
data_file_out_path = './nasa/out/'

file0='OMI-Aura_L3-OMUVBd_2020m0501_v003-2020m0505t093001.he5'
file1='OMI-Aura_L3-OMUVBd_2020m0502_v003-2020m0506t093001.he5'

Val = np.zeros((180, 360), dtype=float)
Tmp0 = np.zeros((180*360), dtype=float)
Tmp1 = np.zeros((180*360), dtype=float)

NUM = int(180*360)

fname =file0.split('_v003')[0]

f = h5py.File(data_file_path+file0,'r')
Tmp0 = np.array(f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/ErythemalDailyDose'][:][:].flatten())

f = h5py.File(data_file_path+file1,'r')
Tmp1 = np.array(f['HDFEOS/GRIDS/OMI UVB Product/Data Fields/ErythemalDailyDose'][:][:].flatten())

for i in range(NUM):
    val0 = Tmp0[i]
    val1 = Tmp1[i]
    if (val0 < 0):
        if(val1 > 0):
            Tmp1[i] = val1
    else:
        if(val1 > 0):
            Tmp1[i] = (val0 + val1)/2.
        else:
            Tmp1[i] = val0

Val=np.reshape(Tmp1,(180,360))

countries = pos.countries.keys()

csvRow =[]
for country in countries:
    Lat = int(float(pos.countries[country][0]))+90
    Lon = int(float(pos.countries[country][1]))+180
    csvRow.append([country,Val[Lat,Lon]])

with open('UBV200501.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csvRow)

