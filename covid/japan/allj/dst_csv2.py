'''
   dst -> csv2

2020-07-02 Ichiro Yoshida
'''
import os
import math
import csv
import numpy as np
import pandas as pd

json_path = './data/json/'
csv_path = './data/csv2/'
pref_data = './data/pref_data.csv'

PrefDF = pd.read_csv(pref_data, index_col=0)
prefs = PrefDF.index
prefs_list = prefs.values.tolist()
pref_pop = PrefDF['popNum']
pref_pop_list = pref_pop.values.tolist()

def td7(n0, n1):
    if (n0 >0 and n1>0): 
        try:
            Td7 = 7.0*math.log(2)/math.log(n1/n0)
        except:
            Td7 = np.nan
    else:
        Td7 = np.nan
    return(Td7)

def ReproductionN(n0, n1):
    if (n0 >0 and n1>0):
        try:
            Rt = (n1/n0) ** (5/7)
        except:
            Rt = np.nan
    else:
        Rt = np.nan
    return(Rt)
    
def conv7(data):
    ave = np.convolve(data, np.ones(7)/float(7), 'valid')
    return(ave[0])

files = os.listdir(json_path)
files.sort()
file = files[-1]

df = pd.read_pickle(json_path+file)
df2 = df.swaplevel('date','name')
df3 = df2.droplevel('name_jp').sort_index()

areas = df3.index.levels[0].tolist()
#areas =['Hokkaido','Tokyo','Aichi','Osaka','Fukuoka','Zenkoku']

for area in areas:
    idx = prefs_list.index(area)
    popNum = float(pref_pop_list[idx])/100000

    df4 = df3.loc[(area)]
    df5 = df4[['npatients','ndeaths']]       #B,C
    data = df5.copy()
#---------------Cases Total(7Ave)-----
    confirmed = data['npatients']            #B
    conf = confirmed.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while (len(conf)-7):
       dat = conf[:7]
       ave7 = conv7(dat)
       data_list=np.append(data_list, ave7)
       del conf[:1]

    data['Cases Total(Ave7)']= data_list #D
#----------------Cases Day----------
    confirmed = data['npatients']            #B
    conf = confirmed.values.tolist()
    diff_list = np.zeros(1)
    diff_list[:] = np.nan
    while (len(conf)-1):
            con = conf[:2]
            diff = int(con[1])-int(con[0])
            diff_list = np.append(diff_list, diff)
            del conf[:1]

    data['Cases Day'] = diff_list           #F
#---------------Cases Day(7Ave)-----
    cases = data['Cases Day']
    case = cases.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while (len(case)-7):
       dat = case[:7]
       ave7 = conv7(dat)
       data_list=np.append(data_list, ave7)
       del case[:1]

    data['Cases Day(Ave7)']= data_list       #G
    data['Cases /100000Pop.'] = data_list / popNum  #H
#---------------Deaths Total(7Ave)-----
    deaths = data['ndeaths']                 #C
    dead = deaths.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while (len(dead)-7):
        dat = dead[:7]
        ave7 = conv7(dat)
        data_list = np.append(data_list, ave7)
        del dead[:1]

    data['Deaths Total(Ave7)']=data_list     #E
#--------------Deaths Day ---
    deaths = data['ndeaths']                 #C
    dead = deaths.values.tolist()
    diff_list = np.zeros(1)
    diff_list[:] = np.nan
    while (len(dead)-1):
        dea = dead[:2]
        try:
            diff = int(dea[1])-int(dea[0])
        except ValueError:
            diff = np.nan

        diff_list = np.append(diff_list, diff)
        del dead[:1]

    data['Deaths Day'] = diff_list           #I
#--------------Deaths Day(7Ave)---
    death = data['Deaths Day']
    dead = death.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while (len(dead)-7):
        dat = dead[:7]
        ave7 = conv7(dat)
        data_list=np.append(data_list, ave7)
        del dead[:1]

    data['Deaths Day(Ave7)'] = data_list   #J
    data['Deaths /100000Pop.'] = data_list/popNum  #K
#--------------Td7,R0,K value,CFR--------
    cases = data['Cases Total(Ave7)']
    cases2 = data['Cases Day(Ave7)']
    case = cases.values.tolist()
    case2 = cases2.values.tolist()
    deaths = data['Deaths Total(Ave7)']
    dead = deaths.values.tolist()

    data_list = np.zeros(7)
    data_list[:] = np.nan
    Td7_list = np.zeros(7)
    Td7_list[:] = np.nan
    R0_list = np.zeros(7)
    R0_list[:] = np.nan
    K_list = np.zeros(7)
    K_list[:]=np.nan

    while(len(case)-7):
        dat=case[:7]
        dat2 = case2[:7]
        n0 = dat[0]
        n1 = dat[6]
        nn0 = dat2[0]
        nn1 = dat2[6]
 
        if(nn0>0):
           R0 = ReproductionN(nn0, nn1)
        else:
           R0 = np.nan

        if(n0):
            if(n0<n1):
               Td7 = td7(n0, n1)
            else:
               Td7 = np.nan 
        else:
           Td7 = np.nan

        Td7_list = np.append(Td7_list, Td7)
        R0_list = np.append(R0_list, R0)
        del case[:1]
        del case2[:1]

    data['Td7']=Td7_list                       #L
    data['Rt']=R0_list                         #M
    data['CFR'] = deaths/cases                 #N 

    file_name = csv_path+area+'.csv'
    print(file_name)
    data.to_csv(file_name,float_format="%.3f")
