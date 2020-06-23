'''
pickle file(.zip) -> csv (Pandas)

2020-06-23 Ichiro Yoshida
'''
import os
import math
import numpy as np
import pandas as pd
import datetime
from pytz import timezone

data_col = 17

dst_path = './data/dst/'
pic_path = './data/pomber/'
wm_path = './data/wmp/'

now = datetime.datetime.now(timezone('UTC'))
now_utc = now.strftime('%Y%m%d_%H%M%S')

def td7(n0, n1):
    return(7.0*math.log(2)/(math.log(n1/n0)))

def ReproductionN(td7):
    k = math.log(2)/td7
    r = math.exp(k * 7.0)
    return(r)

def Kval(n0, n1): #Takashi Nakano Osaka. Univ.
    return(1-(n0/n1))

def conv7(data):
    ave = np.convolve(data, np.ones(7)/float(7), 'valid')
    return(ave)

iso3 = pd.read_csv('./data/code/country_iso3.csv')

files = os.listdir(pic_path)
files.sort()

file = files[-1]

df = pd.read_pickle(pic_path+file)
countries = df.index.levels[0].tolist()

files = os.listdir(wm_path)
files.sort()
file = files[-1]

wm = pd.read_pickle(wm_path+file)


wm_iso3 = pd.merge(wm, iso3, left_on = 'Country', right_on='worldmeters country name')

del wm_iso3['worldmeters country name']

pom_countries = wm_iso3['pomber(GitHub) country name']
pom_countries_list = pom_countries.values.tolist()
wm_countries = wm_iso3['Country']
wm_countries_list = wm_countries.values.tolist()
wm_pop = wm_iso3['Population']
wm_pop_list = wm_pop.values.tolist()

dd = np.zeros(data_col)
dd[:] = np.nan

for country in countries:
    try:
        idx = pom_countries_list.index(country)
        wm_country = wm_countries_list[idx]
        popMil = float(wm_pop_list[idx])/1000000

    except ValueError:
        pass

    data0 = df.loc[(country)].copy()
    data1 =data0.reset_index()
    data1.insert(0,'Country',wm_country)

    data = data1.copy()
    
#---------------Cases Total(7Ave)-----
    confirmed = data['confirmed']
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
    confirmed = data['confirmed']
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
    deaths = data['deaths']
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
    deaths = data['deaths']
    dead = deaths.values.tolist()
    diff_list = np.zeros(1)
    diff_list[:] = np.nan
    while (len(dead)-1):
        dea = dead[:2]
        diff = int(dea[1])-int(dea[0])
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
#--------------Deaths Weekly/1M pop(7Ave)--
    death = data['Deaths Total(Ave7)']
    dead = deaths.values.tolist()
    data_list = np.zeros(7)
    data_list[:] = np.nan
    while(len(dead)-7):
        dat = dead[:7]
        day0 =dat[0]
        day1 =dat[6]
        dif = day1 - day0
        data_list=np.append(data_list, dif)
        del dead[:1]
    data['Deaths Weekly(Ave7)/1M pop']=data_list/popMil
#--------------Deaths /1M pop----
    death = data['Deaths Total(Ave7)']
    dead = deaths.values.tolist()
    num = len(dead)
    dead2 = np.zeros(num)
    dead2[:] = np.nan
    dead2 = np.array(dead)
    dead2 = dead2 / popMil
    data['Deaths /1M pop (Ave7)']=dead2
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
               R0  = ReproductionN(Td7)
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

    a_df  = data.values
    dd = np.vstack([dd,a_df])

dd = np.delete(dd,0,0)

Index=['Country', 'date', 'confirmed', 'deaths', 'recovered',
       'Cases Total(Ave7)', 'Cases Day', 'Cases Day(Ave7)',
       'Deaths Total(Ave7)', 'Deaths Day', 'Deaths Day(Ave7)',
       'Deaths Weekly(Ave7)/1M pop', 'Deaths /1M pop (Ave7)',
       'Td7', 'R0','K','CFR']

new_df0 = pd.DataFrame(dd,columns=Index)
new_df = new_df0.set_index(['Country','date'])

pic_file = './data/dst/'+now_utc+'.zip'
print(pic_file)
new_df.to_pickle(pic_file)

