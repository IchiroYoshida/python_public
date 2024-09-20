'''
./csv/AllLogs.csv and *.png ---> UriyasaMA.kml
2024/09/20
'''
import simplekml
import csv
import os

CSV = './csv/AllLogs.csv'
PNG = './png/'
KML = './kml/UriyasaMA.kml'

githuburl = 'https://raw.githubusercontent.com/IchiroYoshida/python_public/master/uriyasa/png/'
str1 = '<table><tr><td><img src=\"'
str2 = 'width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>'

kml = simplekml.Kml()
kml.document.name ="Diving Logs of Uriyasa 2024"

with open(CSV, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]

for MA in range(30):
    fol = kml.newfolder(name='月齢 '+str(MA))
    for dat in data[1:]:
        MoonAge = float(dat[1]) #MoonAge
        if (MA <= MoonAge < (MA+1)):
            Date   = dat[0] #Date
            DayNo  = dat[2] #Tanks of the day
            EntT   = dat[3] #Entry Time
            EntLat = float(dat[4]) #Entry Latitude
            EntLng = float(dat[5]) #Entry Longitude
            ExtT   = dat[6] #Exit Time
            try:
                ExtLat =float(dat[7]) #Exit Latitude
                ExtLng = float(dat[8]) #Exit Longitude
                Style = 'D'
            except:
                Style = 'A'
            date0 = Date.replace('/','')
            Name = Date+' No.'+DayNo
            NamePNG = date0+'N'+DayNo+'.png'
            str3 = '</table></td>/</tr></table'
            desstr = str1+githuburl+NamePNG+'\"'+str2+str3

            if(Style == 'D'):   
                MidLat = '{:.4f}'.format((EntLat+ExtLat)/2.)
                MidLng = '{:.4f}'.format((EntLng+ExtLng)/2.)

                Entry = [(EntLng, EntLat)]
                Exit  = [(ExtLng, ExtLat)]
                Mid   = [(MidLng, MidLat)]
                Track = Entry + Exit
                print(Name,Entry,Mid,Exit)

                #Entry point
                ent = fol.newpoint()
                ent.coords = Entry
                ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'

                mid = fol.newpoint(name=Name, description = desstr)
                mid.coords = Mid
                mid.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'

                #ext = fol.newpoint(name=NameDN+' Exit')
                ext = fol.newpoint()
                ext.coords = Exit
                ext.iconstyle.icon.href ='http://earth.google.com/images/kml-icons/track-directional/track-none.png'
           
                trk  = fol.newlinestring(name=Name, coords=Track )
                if (EntLat < ExtLat) : #Go North!
                    trk.style.linestyle.color = simplekml.Color.magenta
                else: # Go South!
                    trk.style.linestyle.color = simplekml.Color.cyan
                trk.linestyle.width = 3
            else: # Style = 'A' Anchor
                Entry = [(EntLng, EntLat)]
            print(Name,Entry)
            
            ent = fol.newpoint(name=Name, description = desstr)
            ent.coords = Entry
            ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'    
kml.save(KML)
