# 気象庁　潮位掲載地点一覧表からの主要４分潮の読み込み
# 2023-08-13 Ichiro Yoshida
year = '2023'
position = '唐津'

import pandas as pd

year_filename = './'+year+'/'+year+'.csv'
df = pd.read_csv(year_filename)

data = df[df['掲載地点名'].isin([position])]
lat = data['緯度'].str.split('゜').to_list()[0]

lat0 = int(lat[0])
lat1 = lat[1].replace('\'','')
Lat  = int(lat0)+int(lat1)/60.

lng = df['経度'].str.split('゜').to_list()[0]
lng0 = int(lng[0])
lng1 = lng[1].replace('\'','')
Lng  = int(lng0)+int(lng1)/60.

M2_hr = data['M2振幅'].to_list()[0]
M2_pl = data['M2遅角'].to_list()[0]

S2_hr = data['S2振幅'].to_list()[0]
S2_pl = data['S2遅角'].to_list()[0]

K1_hr = data['K1振幅'].to_list()[0]
K1_pl = data['K1角度'].to_list()[0]

O1_hr = data['O1振幅'].to_list()[0]
O1_pl = data['O1遅角'].to_list()[0]

print(year,position)
print(Lat,Lng)
print('M2 =',M2_hr,M2_pl)
print('S2 =',S2_hr,S2_pl)
print('K1 =',K1_hr,K1_pl)
print('O1 =',O1_hr,O1_pl)
