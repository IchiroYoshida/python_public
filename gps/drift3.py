import simplekml
import csv

kml = simplekml.Kml()
kml.document.name ="Diving Log"

filename = 'Log1.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]

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
        EntLaM  = dat[10] #Entry Latitude minite
        EntLng  = dat[11] #Entry Longitude
        EntLnM  = dat[12] #Entry Longitude minite
        ExtLat  = dat[13] #Exit Latitude
        ExtLaM  = dat[14] #Exit Latitude minite
        ExtLng  = dat[15] #Exit Longitude
        ExtLnM  = dat[16] #Exit Longitude minite
        
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
            ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png'

            mid = kml.newpoint(name=NameMA)
            mid.coords = Mid
            mid.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'

            ext = kml.newpoint(name=NameDN+' Exit')
            ext.coords = Exit
            ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png'


            trk  = kml.newlinestring(name=NameDN+'MA:'+MoonAge, coords=Track )
            trk.style.linestyle.color = simplekml.Color.yellow
            trk.linestyle.width = 3

kml.save('driftMA0.kml')