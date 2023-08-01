import folium
import csv

Tile ="https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg"

githuburl = "https://raw.githubusercontent.com/IchiroYoshida/python_public/master/gps/png/"
str1 = "<table><tr><td><img src=\""
str2 = "width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>"

center =[24.301, 123.986]

filename = 'MALog.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader] #[:50]

for MA in range(15):
    fmap1 = folium.Map(
        location = center,
        tiles = Tile,
        attr = "地理院地図",
        zoom_start = 12,
        width = 1024, height = 800
    )
    htmfile = './html2/UriyasaLogs_MA'+'{0:02}'.format(MA)+'.html'
    print(htmfile)
    for dat in data[1:]:
        MoonAge = float(dat[0]) #MoonAge
        if (MoonAge > 15.):
            MoonAge2 = MoonAge - 15.
        else:
            MoonAge2 = MoonAge
         
        if (MA <= MoonAge2 < (MA+1)):
            date    = dat[1].replace(' ','') #Date
            SerNo   = dat[2].replace(' ','') #Serial Number
            DayNo   = dat[3].replace(' ','') #Tanks of the day
            #Loc     = dat[4] #Location
            Style   = dat[6].replace(' ','') #Anchoring or Drift diving
            EntT    = dat[7].replace(' ','') #Entry Time
            ExtT    = dat[8].replace(' ','') #Exit Time
            EntLat  = dat[9] #Entry Latitude 
            EntLaM  = dat[10] #Entry Latitude minutes
            EntLng  = dat[11] #Entry Longitude
            EntLnM  = dat[12] #Entry Longitude minutes
            ExtLat  = dat[13] #Exit Latitude
            ExtLaM  = dat[14] #Exit Latitude minutes
            ExtLng  = dat[15] #Exit Longitude
            ExtLnM  = dat[16] #Exit Longitude minutes
            
            Name = date + ' No.' + DayNo + ' Ser.' + SerNo
            
            Date = date.replace('/','')
            FName = Date+'N'+DayNo+'.png'
            str3 = '<center>'+Name+' </center></table></td></tr></table'
            desstr = str1+githuburl+FName+'\"'+str2+str3
            
            if (Style == 'D'):
                print(MA,MoonAge,date,SerNo)
                EntLatPos = int(EntLat)+float(EntLaM)/60.
                EntLngPos = int(EntLng)+float(EntLnM)/60.
                ExtLatPos = int(ExtLat)+float(ExtLaM)/60.
                ExtLngPos = int(ExtLng)+float(ExtLnM)/60.
                
                Entry = [EntLatPos, EntLngPos] #[(EntLngPos, EntLatPos)]
                Exit  = [ExtLatPos, ExtLngPos] #[(ExtLngPos, ExtLatPos)]
                
                #Entry point
                folium.Marker(location=Entry,popup=desstr,icon=folium.Icon("orange")).add_to(fmap1)
                
                if (EntLatPos < ExtLatPos) : #Go North!
                    folium.PolyLine([Entry, Exit], color='#FF00FF', weight=3).add_to(fmap1)
                else: # Go South!
                    folium.PolyLine([Entry, Exit], color='#00FFFF', weight=3).add_to(fmap1)

    fmap1.save(htmfile)
