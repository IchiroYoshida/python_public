import simplekml

kml=simplekml.Kml()
kml.document.name ="DivingLog1"

Name  = '2023-05-23 No.1'
Entry = [(124.3490, 24.5653)]
Exit  = [(124.3571, 24.5836)]
Track = Entry + Exit

Mid_lon = (Entry[0][0]+Exit[0][0])/2
Mid_lat = (Entry[0][1]+Exit[0][1])/2

Mid =[(Mid_lon, Mid_lat)]

ent = kml.newpoint(name=Name+' Entry')
ent.coords = Entry
ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png'

mid = kml.newpoint(name=Name)
mid.coords = Mid
mid.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'

ext = kml.newpoint(name=Name+' Exit')
ext.coords = Exit
ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png'


trk  = kml.newlinestring(name=Name, coords=Track )
trk.style.linestyle.color = simplekml.Color.yellow
trk.linestyle.width = 3

kml.save('drift.kml')
