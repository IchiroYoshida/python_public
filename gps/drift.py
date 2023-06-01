import simplekml
#import csv
import pandas as pd

kml = simplekml.Kml()
kml.document.name ="Diving Log"

df = pd.read_csv('Log1.csv', index_col = ["Ser.No."], header=0)

#Index(['月齢', '日時', 'Day.No.', '場所', '通称', 'Style', '開始時刻', '終了時刻', '開始ー北緯度',
#       '開始ー北緯分', '開始ー緯度度', '開始ー緯度分', '終了ー北緯度', '終了ー北緯分', '終了ー緯度度', '終了ー緯度分'],

df['開始ー北緯'] = df['開始ー北緯度'].astype(float)  + df['開始ー緯度分'].astype(float)/60.
df['開始ー経度'] = df[ 
nums = df.index.values.tolist()
for n in nums:
   print(df[n])

for dat in data[1:]:
        MoonAge = dat[0] #MoonAge
        Date    = dat[1] #Date
        SerNo   = dat[2] #Serial Number
        DayNo   = dat[3] #Tanks of the day
        #Loc     = dat[4] #Location
        Style   = dat[6] #Anchoring or Drift diving
        EntT    = dat[7] #Entry Time
        ExtT    = dat[8] #Exit Time
        EntLat  = dat[9] #Entry Latitude 
        EntLaM  = dat[10] #Entry Latitude minutes
        EntLng  = dat[11] #Entry Longitude
        EntLnM  = dat[12] #Entry Longitude minutes
        ExtLat  = dat[13] #Exit Latitude
        ExtLaM  = dat[14] #Exit Latitude minutes
        ExtLng  = dat[15] #Exit Longitude
        ExtLnM  = dat[16] #Exit Longitude minutes
        
        if (Style == 'D'):
            EntLatPos = int(EntLat)+float(EntLaM)/60.
            EntLngPos = int(EntLng)+float(EntLnM)/60.
            ExtLatPos = int(ExtLat)+float(ExtLaM)/60.
            ExtLngPos = int(ExtLng)+float(ExtLnM)/60.
            MidLatPos = (EntLatPos + ExtLatPos)/2.
            MidLngPos = (EntLngPos + ExtLngPos)/2.
        
            NameMA = Date + 'MA: '+MoonAge
            NameDN = Date + 'No.' + DayNo
            Entry = [(EntLngPos, EntLatPos)]
            Exit  = [(ExtLngPos, ExtLatPos)]
            Mid   = [(MidLngPos, MidLatPos)]
            Track = Entry + Exit

            ent = kml.newpoint(name=NameDN+' Entry')
            ent.coords = Entry
            ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'

            mid = kml.newpoint(name=NameMA)
            mid.coords = Mid
            mid.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'

            ext = kml.newpoint(name=NameDN+' Exit')
            ext.coords = Exit
            ext.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/track-none.png'


            trk  = kml.newlinestring(name=NameDN+'MA:'+MoonAge, coords=Track )
            trk.style.linestyle.color = simplekml.Color.yellow
            trk.linestyle.width = 3

kml.save('driftMA0.kml')
'''

