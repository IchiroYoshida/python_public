import csv
import numpy as np
import pandas as pd

#DIR   = './td/2011/'
DIR = './td/2024/'

CompSymb  = ['Sa','Ssa','Mm','MSf','Mf','2Q1','Sig1','Q1','Rho1','O1','MP1','M1', \
             'Chi1','Pi1','P1','S1','K1','Psi1','Phi1','The1','J1','SO1','OO1','OQ2', \
             'MNS2','2N2','Mu2','N2','Nu2','OP2','M2','MKS2','Lam2','L2',\
             'T2','S2','R2','K2','MSN2','KJ2','2SM2','MO3','M3','SO3',\
             'MK3','SK3', 'MN4','M4','SN4','MS4','MK4','S4','SK4','2MN6',\
             'M6','MSN6','2MS6','2MK6','2SM6','MSK6']

class TD3(object):
    def __init__(self,pname):
        file_td3 = DIR+pname+'.TD3'
        
        self.harms = pd.DataFrame(np.zeros(60*2,np.float64).reshape(60,2),columns=['pl','hr'],index=CompSymb)
        
        with open(file_td3, encoding='utf8', newline='') as f:
            csvreader = csv.reader(f)
            lin = next(csvreader)
            self.label = pd.Series(lin,index=['Name','Latitude','Longitude','Level'])
       
            elements = [row for row in csvreader]
            
            for n in range(len(elements)):
                element = elements[n]
                key1 = str(element[0]).replace(' ','')
                self.harms['hr'][key1]  = float(element[1])
                self.harms['pl'][key1]  = float(element[2])
                key2 = str(element[3]).replace(' ','')
                self.harms['hr'][key2]  = float(element[4])
                self.harms['pl'][key2]  = float(element[5])

if __name__ == '__main__':
    name = '石垣'

    td3 = TD3(name)

    print(name)
    print(td3.label)
    print(td3.harms['pl'])
    print(td3.harms['hr'])
