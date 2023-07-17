import simplekml
import csv

kml = simplekml.Kml()
kml.document.name ="Diving Logs"

filename = 'MALog.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]

for MA in range(15):
    fol = kml.newfolder(name='MA'+str(MA))
    for dat in data[1:]:
        MoonAge = float(dat[0]) #MoonAge
        if (MoonAge > 15.):
            MoonAge2 = MoonAge - 15.
        else:
            MoonAge2 = MoonAge
         
        if (MA <= MoonAge2 < (MA+1)):
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
                print(MA,dat[1],dat[2])
                EntLatPos = int(EntLat)+float(EntLaM)/60.
                EntLngPos = int(EntLng)+float(EntLnM)/60.
                ExtLatPos = int(ExtLat)+float(ExtLaM)/60.
                ExtLngPos = int(ExtLng)+float(ExtLnM)/60.
                MidLatPos = (EntLatPos + ExtLatPos)/2.
                MidLngPos = (EntLngPos + ExtLngPos)/2.
        
                Name = ' MA: '+str(MoonAge) + '  ' + Date + ' No.' + DayNo + ' Ser.' + SerNo
                Entry = [(EntLngPos, EntLatPos)]
                Exit  = [(ExtLngPos, ExtLatPos)]
                Mid   = [(MidLngPos, MidLatPos)]
                Track = Entry + Exit

                #ent = fol.newpoint(name=NameDN+' Entry')
                ent = fol.newpoint()
                ent.coords = Entry
                ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'

                mid = fol.newpoint(name=Name)
                mid.coords = Mid
                mid.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'

                #ext = fol.newpoint(name=NameDN+' Exit')
                ext = fol.newpoint()
                ext.coords = Exit
                ext.iconstyle.icon.href ='http://earth.google.com/images/kml-icons/track-directional/track-none.png'

                trk  = fol.newlinestring(name=Name, coords=Track )
                if (EntLatPos < ExtLatPos) : #Go North!
                    trk.style.linestyle.color = simplekml.Color.magenta
                else: # Go South!
                    trk.style.linestyle.color = simplekml.Color.cyan
                trk.linestyle.width = 3

kml.save('driftMA2.kml')
