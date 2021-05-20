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
pref_data = './data/pref_data.csv'

PrefDF = pd.read_csv(pref_data, index_col=0)
prefs = PrefDF.index
prefs_list = prefs.values.tolist()
pref_pop = PrefDF['popNum']
pref_pop_list = pref_pop.values.tolist()

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

def caseAve7(data):
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

def totalAve7(data):
    try:
        ave = np.convolve(data, np.ones(7)/float(7), 'valid')
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
for d in range(len(dates)-13):
    csvRow = []
    date1 = dates[d+13]
    date0 = dates[d]
    
    dd3=df2.swaplevel('date','name')
    for area in areas:                              #A
        idx = prefs_list.index(area)
        popNum = float(pref_pop_list[idx])/100000
        
        areaData = dd3.loc[(area)]
        areaData2 = areaData[['npatients','ndeaths']]
        data0 = areaData2[:7].copy()
        data1 = areaData2[7:14].copy()
        
#----------------Cases Day(7Ave)----------
        confirmed0 = data0['npatients']
        conf0 = confirmed0.values.tolist()
        totalAve7_n0 = totalAve7(conf0)
        caseAve7_n0 = caseAve7(conf0)
        
        confirmed1= data1['npatients']
        conf1 = confirmed1.values.tolist()
        totalAve7_n1 = totalAve7(conf1)
        caseAve7_n1 = caseAve7(conf1)
        conf1 = confirmed1.values.tolist()
        
        npatients = conf1[6]                          #B
        TotalCasesAve7 = totalAve7_n1                 #D
        CasesAve7 = caseAve7_n1                       #G
        CasesPop = caseAve7_n1 /popNum                #H
        Cases = conf1[6] - conf1[5]                   #F
      
#--------------Deaths Day(7Ave)-------------
        deaths = data1['ndeaths']
        dead = deaths.values.tolist()
        DeathsAve7 = caseAve7(dead)                   #J
        TotalDeathsAve7 = totalAve7(dead)             #E
        dead = deaths.values.tolist()
        ndeaths = dead[6]                             #C
        DeathsPop = DeathsAve7 /popNum                 #K
        Deaths = dead[6]-dead[5]                      #I
#--------------Td7,Rt,K value,CFR--------        
        Rt = ReproductionN(caseAve7_n0, caseAve7_n1)  #M
        Td7 = td7(totalAve7_n0, totalAve7_n1)         #L

        if(caseAve7_n1 >0):
            try:
                CFR = DeathsAve7/CasesAve7            #N
            except:
                CFR = np.nan
        csvRow.append([area,npatients,ndeaths,                 #A,B,C
                       TotalCasesAve7, TotalDeathsAve7,        #D,E,
                       Cases,CasesAve7,CasesPop,               #F,G,H
                       Deaths,DeathsAve7,DeathsPop,            #I,J,K
                       Td7,Rt,CFR])                            #L,M,N
        files_df = pd.DataFrame({date0:csvRow}) 
    df2=df2.drop(index=date0)

print(files_df)
'''   
    file_name = csv_path+date1+'.csv'
    
    with open(file_name, 'w', encoding='utf-8') as f:
        writer =csv.writer(f)
        writer.writerow(['Pref.','npatients','ndeaths',
                         'Total cases(ave7)','Total deaths(ave7)',
                         'Daily cases','cases(ave7)','cases/100000pop.',
                         'Daily deaths','deaths(ave7)','deaths/10000pop.',
                         'Td7','Rt','CFR'])
        writer.writerows(csvRow)
        print(file_name)
'''
