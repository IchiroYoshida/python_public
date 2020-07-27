'''
   dst -> csv2

2020-07-02 Ichiro Yoshida
'''
import os
import math
import numpy as np
import pandas as pd

json_path = './data/json/'
csv_path = './data/csv2/'

def td7(n0, n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

#def ReproductionN(td7):
#    k = math.log(2)/td7
#    r = math.exp(k * 7.0)
#    return(r)

def ReproductionN(n0, n1):
    return((n1/n0) ** (5/7))

def Kval(n0, n1): #Takashi Nakano Osaka. Univ.
    return(1-(n0/n1))

def conv7(data):
    ave = np.convolve(data, np.ones(7)/float(7), 'valid')
    return(ave)

files = os.listdir(json_path)
files.sort()
file = files[-1]

df = pd.read_pickle(json_path+file)

df2 = df.swaplevel('date','name')
df3 = df2.droplevel('name_jp').sort_index()

areas = df3.index.levels[0].tolist()

for area in areas:
    df4 = df3.loc[(area)]
    df5 = df4[['npatients','ndeaths']]
    data = df5.copy()
#---------------Cases Total(7Ave)-----
    confirmed = data['npatients']
    conf = confirmed.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while (len(conf)-7):
       dat = conf[:7]
       ave7 = conv7(dat)
       data_list=np.append(data_list, ave7)
       del conf[:1]

    data['Cases Total(Ave7)']= data_list
#----------------Cases Day----------
    confirmed = data['npatients']
    conf = confirmed.values.tolist()
    diff_list = np.zeros(1)
    diff_list[:] = np.nan
    while (len(conf)-1):
            con = conf[:2]
            diff = int(con[1])-int(con[0])
            diff_list = np.append(diff_list, diff)
            del conf[:1]

    data['Cases Day'] = diff_list
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

    data['Cases Day(Ave7)']= data_list
#---------------Deaths Total(7Ave)-----
    deaths = data['ndeaths']
    dead = deaths.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while (len(dead)-7):
        dat = dead[:7]
        ave7 = conv7(dat)
        data_list = np.append(data_list, ave7)
        del dead[:1]

    data['Deaths Total(Ave7)']=data_list
#--------------Deaths Day ---
    deaths = data['ndeaths']
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

    data['Deaths Day'] = diff_list
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

    data['Deaths Day(Ave7)'] = data_list
#--------------Td7,R0,K value,CFR--------
    cases = data['Cases Total(Ave7)']
    case = cases.values.tolist()
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
        n0 = dat[0]
        n1 = dat[6]

        if(n0):
            if(n0<n1):
               Td7 = td7(n0, n1)
               R0  = ReproductionN(n0, n1)
               K   = Kval(n0, n1)
            else:
               Td7 = np.nan 
               R0  = np.nan
               K   = np.nan
        else:
           Td7 = np.nan
           R0  = np.nan
           K   = np.nan

        Td7_list = np.append(Td7_list, Td7)
        R0_list = np.append(R0_list, R0)
        K_list = np.append(K_list, K)
        del case[:1]

    data['Td7']=Td7_list
    data['R0']=R0_list
    data['K']=K_list
    data['CFR'] = deaths/cases 

    file_name = csv_path+area+'.csv'
    print(file_name)
    data.to_csv(file_name)
