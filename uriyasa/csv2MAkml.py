'''
./csv/AllLogs.csv and *.png ---> UriyasaMA.kml
2024/05/13
'''
import simplekml
import csv
import os

CSV = './csv/AllLogs.csv'
PNG = './png/'
KML = './kml/Uriyasa2025.kml'

githuburl = 'https://raw.githubusercontent.com/IchiroYoshida/python_public/master/uriyasa/png/'
str1 = '<table><tr><td><img src=\"'
str2 = 'width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>'

kml = simplekml.Kml()
kml.document.name ="Diving Logs of Uriyasa 2003 - 2025."

with open(CSV, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]
    del data[:1] #Remove CSV header
    
for MA in range(30):
    fol = kml.newfolder(name='月齢 '+str(MA))
    for dat in data:
        MoonAge = float(dat[2]) #MoonAge
        if (MA <= MoonAge < (MA+1)):
            Date   = dat[1] #Date
            DayNo  = dat[3] #Tanks of the day
            EntT   = dat[4] #Entry Time
            EntLat = float(dat[5]) #Entry Latitude
            EntLng = float(dat[6]) #Entry Longitude
            ExtT   = dat[7] #Exit Time
            try:
                ExtLat =float(dat[8]) #Exit Latitude
                ExtLng = float(dat[9]) #Exit Longitude
                Style = 'D'
            except:
                Style = 'A'
            date0 = Date.replace('/','')
            Name = Date+' No.'+DayNo
            NamePNG = date0+'N'+DayNo+'.png'
            str3 = '</table></td>/</tr></table'
            desstr = str1+githuburl+NamePNG+'\"'+str2+str3

            if(Style == 'D'):   
                Entry = [(EntLng, EntLat)]
                Exit  = [(ExtLng, ExtLat)]
                Track = Entry + Exit
                print(Name,Entry,Exit)

                #Entry point
                ent = fol.newpoint(name=Name, description = desstr)
                ent.coords = Entry
                ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'

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
                ent = fol.newpoint(name=Name, description = desstr)
                ent.coords = Entry
                ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'
                print(Name,Entry)
kml.save(KML)
