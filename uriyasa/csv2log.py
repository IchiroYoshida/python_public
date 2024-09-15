'''
MALog.csv -->  *.log
2024/09/15

'''

import csv

filename = 'MALog.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]

for dat in data[1:]:
    MA = dat[0] #MoonAge
    Date    = dat[1].replace(' ','').replace('/','') #Date
    #SerNo   = dat[2] #Serial Number
    DayNo   = dat[3] #Tanks of the day
    #Loc     = dat[4] #Location
    Style   = dat[6] #Anchoring or Drift diving
    EntT    = dat[7].replace(' ','') #Entry Time
    ExtT    = dat[8].replace(' ','') #Exit Time
    EntLat  = dat[9].replace(' ','') #Entry Latitude 
    EntLaM  = dat[10].replace(' ','') #Entry Latitude minutes
    EntLng  = dat[11].replace(' ','') #Entry Longitude
    EntLnM  = dat[12].replace(' ','') #Entry Longitude minutes
    ExtLat  = dat[13].replace(' ','') #Exit Latitude
    ExtLaM  = dat[14].replace(' ','') #Exit Latitude minutes
    ExtLng  = dat[15].replace(' ','') #Exit Longitude
    ExtLnM  = dat[16].replace(' ','') #Exit Longitude minutes
    
    try:
        EntLatPos = "{:.4f}".format(int(EntLat)+float(EntLaM)/60.)
        EntLngPos = "{:.4f}".format(int(EntLng)+float(EntLnM)/60.)
    except:
        continue
       
    if (Style == 'D'):
        ExtLatPos = "{:.4f}".format(int(ExtLat)+float(ExtLaM)/60.)
        ExtLngPos = "{:.4f}".format(int(ExtLng)+float(ExtLnM)/60.)
    else:
        ExtLatPos = None
        ExtLngPos = None
    
    FName = Date+'N'+DayNo
    print(FName,EntT,EntLatPos,EntLngPos,ExtT,ExtLatPos,ExtLngPos)
    
    with open('./LOG/'+FName+'.log','w') as f:
        writer= csv.writer(f)
        writer.writerow([EntT,EntLatPos,EntLngPos,ExtT,ExtLatPos,ExtLngPos])