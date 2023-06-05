# 気象庁　潮位掲載地点一覧表の読み込み Ver 2.0
# 2023-06-03 Ichiro Yoshida
year = '2023'

import pandas as pd
import requests
from bs4 import BeautifulSoup

CompSymb  = ['Sa','Ssa','Mm','MSf','Mf','2Q1','Sig1','Q1','Rho1','O1','MP1','M1', \
             'Chi1','Pi1','P1','S1','K1','Psi1','Phi1','The1','J1','SO1','OO1','OQ2', \
             'MNS2','2N2','Mu2','N2','Nu2','OP2','M2','MKS2','Lam2','L2',\
             'T2','S2','R2','K2','MSN2','KJ2','2SM2','MO3','M3','SO3',\
             'MK3','SK3', 'MN4','M4','SN4','MS4','MK4','S4','SK4','2MN6',\
             'M6','MSN6','2MS6','2MK6','2SM6','MSK6']

url0 = 'http://www.data.jma.go.jp/kaiyou/db/tide/suisan/harms60.php?stn='
url1 = '&year='+year+'&tyear='+year

year_filename = './'+year+'/'+year+'.csv'
df = pd.read_csv(year_filename)

df2 = df[df['分潮一覧表'] == (year+'年')]

lats = df2['緯度'].str.split('゜')
newlats=[]
for lat in lats:
    lat0 = int(lat[0])
    lat1 = lat[1].replace('\'','')
    newlats.append(int(lat0)+int(lat1)/60.)

lngs = df2['経度'].str.split('゜')
newlngs=[]
for lng in lngs:
    lng0 = int(lng[0])
    lng1 = lng[1].replace('\'','')
    newlngs.append(int(lng0)+int(lng1)/60.)
 
positions = df2['地点記号'].values.tolist()
names = df2['掲載地点名'].values.tolist()
MSLs = df2['MSL潮位表基準面'].values.tolist()

for i in range(len(positions)):
    pos = positions[i]
    name = names[i]
    msl = MSLs[i]
    Lat = newlats[i]
    Lng = newlngs[i]
        
    url = url0 + pos + url1
    print(pos,name,url)
    points_html = requests.get(url)
    points = BeautifulSoup(points_html.content, 'html.parser')
    table = points.find('table')

    datas = []
    for tr in table.find_all('tr'):
        datas.append([td.text.strip() for td in tr.find_all('td')])
    data=datas[1:]
    
    file_name = './'+year+'/' + name + '.TD3'
    f = open(file_name,'w')
    
    str = '{0:<},'.format(name)+\
          '{:>8.2f},'.format(Lat)+\
          '{:>8.2f},'.format(Lng)+\
          '{:>5}'.format(msl)+'\n'
    f.write(str)
    
    for n in range(0,60,2):
        str = '{:<4},'.format(CompSymb[n])+\
              '{:>5},'.format(data[n][0])+\
              '{:>6},'.format(data[n][1])+\
              '      '+\
              '{:<4},'.format(CompSymb[n+1])+\
              '{:>5},'.format(data[n+1][0])+\
              '{:>6}'.format(data[n+1][1])+'\n'
        f.write(str)
    f.close()   
