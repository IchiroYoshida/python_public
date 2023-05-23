import simplekml

kml=simplekml.Kml()
kml.document.name ="DivingLog1"

Name  = '2023-05-23 No.1'
Entry = [(124.3490, 24.5653)]
Exit  = [(124.3571, 24.5836)]
Track = Entry + Exit

pnt = kml.newpoint(name=Name+' Entry')
pnt.coords = Entry
pnt.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'
pnt.labelstyle.scale = 0.66

pnt = kml.newpoint(name=Name+' Exit')
pnt.coords = Exit

pnt = kml.newlinestring(name=Name, coords=Track )
pnt.style.linestyle.color = simplekml.Color.yellow
pnt.linestyle.width = 3

kml.save('drift.kml')

