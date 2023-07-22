import simplekml
import csv

githuburl = 'https://raw.githubusercontent.com/IchiroYoshida/python_public/master/gps/png/'
str1 = '<table><tr><td><img src=\"'
str2 = 'width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>'

kml = simplekml.Kml()
kml.document.name ="Diving Logs of Uriyasa 2003-2013."

filename = 'MALog.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]   #[:10]

for MA in range(15):
    fol = kml.newfolder(name='MA'+str(MA))
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
            
            Date = date.replace('/','')
            FName = Date+'N'+DayNo+'.png'
            str3 = '<center>Ser.'+SerNo+' </center></table></td></tr></table'
            desstr = str1+githuburl+FName+'\"'+str2+str3
            
            if (Style == 'D'):
                print(MA,MoonAge,date,SerNo)
                EntLatPos = int(EntLat)+float(EntLaM)/60.
                EntLngPos = int(EntLng)+float(EntLnM)/60.
                ExtLatPos = int(ExtLat)+float(ExtLaM)/60.
                ExtLngPos = int(ExtLng)+float(ExtLnM)/60.
                MidLatPos = (EntLatPos + ExtLatPos)/2.
                MidLngPos = (EntLngPos + ExtLngPos)/2.
        
                Name = ' MA: '+str(MoonAge) + '  ' + date + ' No.' + DayNo + ' Ser.' + SerNo
                Entry = [(EntLngPos, EntLatPos)]
                Exit  = [(ExtLngPos, ExtLatPos)]
                Mid   = [(MidLngPos, MidLatPos)]
                Track = Entry + Exit

                #Entry point.
                ent = fol.newpoint()
                ent.coords = Entry
                ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'

                mid = fol.newpoint(name=Name, description = desstr)
                mid.coords = Mid
                mid.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'

                #Exit point.
                ext = fol.newpoint()
                ext.coords = Exit
                ext.iconstyle.icon.href ='http://earth.google.com/images/kml-icons/track-directional/track-none.png'

                trk  = fol.newlinestring(name=Name, coords=Track )
                if (EntLatPos < ExtLatPos) : #Go North!
                    trk.style.linestyle.color = simplekml.Color.magenta
                else: # Go South!
                    trk.style.linestyle.color = simplekml.Color.cyan
                trk.linestyle.width = 3

kml.save('UriyasaLogs.kml')
