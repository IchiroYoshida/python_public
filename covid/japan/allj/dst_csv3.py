'''
   dst -> csv3

2021-05-08 Ichiro Yoshida
'''
import os
import math
import csv
import numpy as np
import pandas as pd

json_path = './data/json/'
csv_path = './data/csv3/'

def td7(n0, n1):
    if (n0 >0 and n1>0):
        if (n1 > n0):
            try:
                Td7 = 7.0*math.log(2)/math.log(n1/n0)
            except:
                Td7 = np.nan
        else:
            Td7 = np.nan
    else:
        Td7 = np.nan
    return(Td7)

def ReproductionN(n0, n1):
    if (n0>0 and n1>0):
        try:
            rt = (n1/n0) ** (5/7)
        except:
            rt = np.nan
    else:
        rt = np.nan
    return(rt)

def Kval(n0, n1): #Takashi Nakano Osaka. Univ.
    if (n0>0 and n1>0):
        try:
            Kv = 1-(n0/n1)
        except:
            Kv = np.nan
    else:
        Kv = np.nan
    return(Kv)

def ave7(data):
    diff_list = np.zeros(7)
    for d in range(0, 6):
        dat = data[:2]
        try:
            diff = int(dat[1])-int(dat[0])
        except:
            diff = np.nan
        diff_list[d] = diff
        del data[:1]
    try:
        ave = np.convolve(diff_list, np.ones(7)/float(7), 'valid')
    except:
        ave = np.nan
    return(ave[0])
    
files = os.listdir(json_path)
files.sort()
file = files[-1]

df = pd.read_pickle(json_path+file)
df2 = df.droplevel('name_jp')
df3=df2.swaplevel('date','name')
areas = df3.index.levels[0].tolist()
dates = df2.index.levels[0].tolist()
#areas =['Hokkaido','Tokyo','Aichi','Osaka','Fukuoka','Zenkoku']

#for d in range(5):
for d in range(len(dates)-14):
    csvRow = []
    date1 = dates[d+7]
    date0 = dates[d]
    
    dd3=df2.swaplevel('date','name')
    for area in areas:
        areaData = dd3.loc[(area)]
        areaData2 = areaData[['npatients','ndeaths']]
        data0 = areaData2[:7].copy()
        data1 = areaData2[7:14].copy()
        
#----------------Cases Day(7Ave)----------
        confirmed0 = data0['npatients']
        conf0 = confirmed0.values.tolist()
        npat0=conf0[0]
        caseAve7_n0 = ave7(conf0)
        
        confirmed1= data1['npatients']
        conf1 = confirmed1.values.tolist()
        npat1=conf1[0]
        caseAve7_n1 = ave7(conf1)
        
#--------------Deaths Day(7Ave)-------------
        deaths = data0['ndeaths']
        dead = deaths.values.tolist()
        deathAve7 = ave7(dead)
#--------------Td7,Rt,K value,CFR--------        
        Rt = ReproductionN(caseAve7_n0, caseAve7_n1)
        Td7 = td7(npat0, npat1)
        Kv = Kval(npat0, npat1)

        if(caseAve7_n0 >0):
            try:
                CFR = deathAve7/caseAve7_n0
            except:
                CFR = np.nan
        csvRow.append([area,caseAve7_n0,deathAve7,Td7,Rt,Kv,CFR])
    df2=df2.drop(index=date0)

    file_name = csv_path+date1+'.csv'
    
    with open(file_name, 'w', encoding='utf-8') as f:
        writer =csv.writer(f)
        writer.writerow(['Pref.','cases(ave7)','deaths(ave7)','Td','Rt','K','CFR'])
        writer.writerows(csvRow)
        print(file_name)