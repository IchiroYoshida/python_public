'''
JSON Data -> pickle file(.zip) (Pandas)

2020-06-12 Ichiro Yoshida
'''
import math
import numpy as np
import json
import datetime
from pytz import timezone
import requests
import pandas as pd
from bs4 import BeautifulSoup

df_col = 17

csv2_path = './data/csv2/'

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

url='https://pomber.github.io/covid19/timeseries.json'
wmc='https://www.worldometers.info/coronavirus/'

now= datetime.datetime.now(timezone('UTC'))
now_utc = now.strftime('%Y%m%d_%H%M%S')

#----- get pomber(GitHub) countries data ----------
s = requests.Session()
r = s.get(url)

json_data = json.loads(r.text)
countries = list(json_data.keys())

#----- get worldmeter coronavirus countries data ---
# HTML table -> CSV

wm_res = requests.get(wmc)
wm_soup = BeautifulSoup(wm_res.text, 'html.parser')
wm_table = wm_soup.find('table')
wm_data = [dat.text for dat in wm_table('td')]
wm_col = 19   #colums of the worldmeters HTML table

csvRow = []

while len(wm_data):
    row = wm_data[:wm_col]
    del row[:1]
    del row[6]
    del row[-3:]
    csvRow.append(row)
    del wm_data[:wm_col]

del csvRow[:8]   # Delete Head.
del csvRow[-8:]  # Delete Tail.

new_col = 12
newlist = []
while len(csvRow):
    newRow = []
    row = csvRow[:wm_col][0]
    del row[2]
    del row[3]
    newRow.append(row[0])
    del csvRow[:1]
    for dd in range(1,new_col-1):
        new_dat = row[dd].replace(',','').replace(' ','')
        newRow.append(new_dat)
    newlist.append(newRow)

wmp = pd.DataFrame(newlist, columns=['Country','Total Cases','Total Deaths',\
    'Total Recovered','Active Cases','Serious Critical','Tot Cases/1M pop',\
    'Deaths/1M pop','Total Tests','Tests/1M pop','Population'])

wmp_iso = pd.merge(wmp, iso3, how='outer',
        left_on = 'Country', right_on='worldmeters country name')

pom_countries = wmp_iso['pomber(GitHub) country name']
wm_countries  = wmp_iso['worldmeters country name']
wm_pop = wmp_iso['Population']
pom_country_list = pom_countries.values.tolist()
wm_country_list = wm_countries.values.tolist()
wm_pop_list = wm_pop.values.tolist()

dd = np.zeros(df_col)
dd[:] =  np.nan

for i in range(len(countries)):
    country = countries[i]

    try:
        idx = pom_country_list.index(country)
        country_wm = wm_country_list[idx]
        popMil = float(wm_pop_list[idx])/1000000

    except ValueError:
        pass

    if(country_wm is np.nan):
        continue
    else:
        df = pd.json_normalize(json_data, record_path=country)
        df.insert(0,'Country',country_wm)
#---------------Cases Total(7Ave)-----
        confirmed = df['confirmed']
        conf = confirmed.values.tolist()
        data_list = np.zeros(7)
        data_list[:] = np.nan
        while (len(conf)-7):
           dat = conf[:7]
           ave7 = conv7(dat)
           data_list=np.append(data_list, ave7)
           del conf[:1]

        df['Cases Total(Ave7)']= data_list
#----------------Cases Day----------
        confirmed = df['confirmed']
        conf = confirmed.values.tolist()
        diff_list = np.zeros(1)
        diff_list[:] = np.nan
        while (len(conf)-1):
            con = conf[:2]
            diff = int(con[1])-int(con[0])
            diff_list = np.append(diff_list, diff)
            del conf[:1]

        df['Cases Day'] = diff_list
#---------------Cases Day(7Ave)-----
        cases = df['Cases Day']
        case = cases.values.tolist()
        data_list = np.zeros(7)
        data_list[:] = np.nan
        while (len(case)-7):
           dat = case[:7]
           ave7 = conv7(dat)
           data_list=np.append(data_list, ave7)
           del case[:1]

        df['Cases Day(Ave7)']= data_list
#---------------Deaths Total(7Ave)-----
        deaths = df['deaths']
        dead = deaths.values.tolist()
        data_list = np.zeros(7)
        data_list[:] = np.nan
        while (len(dead)-7):
            dat = dead[:7]
            ave7 = conv7(dat)
            data_list = np.append(data_list, ave7)
            del dead[:1]

        df['Deaths Total(Ave7)']=data_list
#--------------Deaths Day ---
        deaths = df['deaths']
        dead = deaths.values.tolist()
        diff_list = np.zeros(1)
        diff_list[:] = np.nan
        while (len(dead)-1):
            dea = dead[:2]
            diff = int(dea[1])-int(dea[0])
            diff_list = np.append(diff_list, diff)
            del dead[:1]

        df['Deaths Day'] = diff_list
#--------------Deaths Day(7Ave)---
        death = df['Deaths Day']
        dead = death.values.tolist()
        data_list = np.zeros(7)
        data_list[:] = np.nan
        while (len(dead)-7):
            dat = dead[:7]
            ave7 = conv7(dat)
            data_list=np.append(data_list, ave7)
            del dead[:1]

        df['Deaths Day(Ave7)'] = data_list
#--------------Deaths Weekly/1M pop(7Ave)--
        death = df['Deaths Total(Ave7)']
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
        df['Deaths Weekly(Ave7)/1M pop']=data_list/popMil
#--------------Deaths /1M pop----
        death = df['Deaths Total(Ave7)']
        dead = deaths.values.tolist()
        num = len(dead)
        dead2 = np.zeros(num)
        dead2[:] = np.nan
        dead2 = np.array(dead)
        dead2 = dead2 / popMil
        df['Deaths /1M pop (Ave7)']=dead2

#--------------Td7,R0,K value--------
        cases = df['Cases Total(Ave7)']
        case = cases.values.tolist()
        deaths = df['Deaths Total(Ave7)']
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

        df['Td7']=Td7_list
        df['R0']=R0_list
        df['K']=K_list
        df['CFR'] = deaths/cases 

    a_df = df.values
    dd = np.vstack([dd,a_df])

dd = np.delete(dd,0,0)

Index=['Country', 'date', 'confirmed', 'deaths', 'recovered',
       'Cases Total(Ave7)', 'Cases Day', 'Cases Day(Ave7)',
       'Deaths Total(Ave7)', 'Deaths Day', 'Deaths Day(Ave7)',
       'Deaths Weekly(Ave7)/1M pop', 'Deaths /1M pop (Ave7)',
       'Td7', 'R0','K','CFR']

new_df = pd.DataFrame(dd,columns=Index)
pic_file = './data/dst/'+now_utc+'.zip'
print(pic_file)
#new_df.to_pickle(pic_file)
