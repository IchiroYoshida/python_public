'''
*.log and *.png ---> *.kml
2024/09/18
'''
import simplekml
import csv
import os

kml = simplekml.Kml()
kml.document.name ="Diving Logs 2023"

FileName = '2023.kml'
LOG = './LOG/2023log/'
#PNG = './PNG/2024png/'
#KML = ''

log_files = os.listdir(LOG)
log_files.sort()

for date in log_files: 
    with open(LOG+date, encoding='utf8', newline='') as l:
        csvreader =csv.reader(l)
        data = [row for row in csvreader][0]
        
        Date = date.replace('.log','').split('N')
        date = Date[0]
        DayNo = Date[1]
        FolderName = date+'N'+DayNo
        fol = kml.newfolder(name=FolderName)
        
        YY = date[:4]  #Year
        MM = date[4:6] #Month
        DD = date[6:]  #Day
        
        EntT   = data[0]  #Entry
        EntLat = float(data[1])
        EntLng = float(data[2])
        
        ExtT   = data[3]  #Exit
        try:
            ExtLat = float(data[4])
            ExtLng = float(data[5])
            Style = 'D'
        except:
            Style = 'A'

        Name = date+' No.'+DayNo
           
        if(Style == 'D'):   
            MidLat = (EntLat+ExtLat)/2.
            MidLng = (EntLng+ExtLng)/2.

            Entry = [(EntLng, EntLat)]
            Exit  = [(ExtLng, ExtLat)]
            Mid   = [(MidLng, MidLat)]
            Track = Entry + Exit
            print(Name,Entry,Mid,Exit)

            #Entry point
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
            if (EntLat < ExtLat) : #Go North!
                trk.style.linestyle.color = simplekml.Color.magenta
            else: # Go South!
                trk.style.linestyle.color = simplekml.Color.cyan
            trk.linestyle.width = 3
        else: # Style = 'A' Anchor
            Entry = [(EntLng, EntLat)]
            print(Name,Entry)
            
            ent = fol.newpoint(name=Name)
            ent.coords = Entry
            ent.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'    
kml.save(FileName)