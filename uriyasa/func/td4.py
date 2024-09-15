import csv
import numpy as np
import pandas as pd

#DIR   = './td/2023/'
year = '2023'

year_filename = './'+year+'/'+year+'.csv'
df = pd.read_csv(year_filename)

CompSymb  = ['Sa','Ssa','Mm','MSf','Mf','2Q1','Sig1','Q1','Rho1','O1','MP1','M1', \
             'Chi1','Pi1','P1','S1','K1','Psi1','Phi1','The1','J1','SO1','OO1','OQ2', \
             'MNS2','2N2','Mu2','N2','Nu2','OP2','M2','MKS2','Lam2','L2',\
             'T2','S2','R2','K2','MSN2','KJ2','2SM2','MO3','M3','SO3',\
             'MK3','SK3', 'MN4','M4','SN4','MS4','MK4','S4','SK4','2MN6',\
             'M6','MSN6','2MS6','2MK6','2SM6','MSK6']

class TD4(object):
    def __init__(self,pname):
        self.harms = pd.DataFrame(np.zeros(60*2,np.float64).reshape(60,2),columns=['pl','hr'],index=CompSymb)
        
        data = df[df['掲載地点名'].isin([pname])]
        lat = data['緯度'].str.split('゜').to_list()[0]

        lat0 = int(lat[0])
        lat1 = lat[1].replace('\'','')
        Lat  = int(lat0)+int(lat1)/60.

        lng = df['経度'].str.split('゜').to_list()[0]
        lng0 = int(lng[0])
        lng1 = lng[1].replace('\'','')
        Lng  = int(lng0)+int(lng1)/60.

        df.at['pl','M2'] = data['M2振幅'].to_list()[0]
        df.at['hr','M2'] = data['M2遅角'].to_list()[0]

        df.at['pl','S2'] = data['S2振幅'].to_list()[0]
        df.at['hr','S2'] = data['S2遅角'].to_list()[0]

        df.at['pl','K1'] = data['K1振幅'].to_list()[0]
        df.at['hr','K1'] = data['K1角度'].to_list()[0]

        df.at['pl','O1'] = data['O1振幅'].to_list()[0]
        df.at['hr','O1'] = data['O1遅角'].to_list()[0]

        #Level!!
        lin = [pname,Lat,Lng,Level]
        self.label = pd.Series(lin,index=['Name','Latitude','Longitude','Level'])
       
if __name__ == '__main__':
    name = '石垣'

    td4 = TD4(name)

    print(name)
    print(td4.label)
    print(td4.harms['pl'])
    print(td4.harms['hr'])
