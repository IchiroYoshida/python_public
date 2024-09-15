'''
show LOG dir files.log 
2024/09/15
'''

import os
import csv

log_files = os.listdir('./LOG')

for date in log_files[:3]:
    with open('./LOG/'+date, encoding='utf8', newline='') as l:
        csvreader =csv.reader(l)
        data = [row for row in csvreader][0]
        
        Date = date.replace('.log','').split('N')
        
        YY = Date[0][:4]  #Year
        MM = Date[0][4:6] #Month
        DD = Date[0][6:]  #Day
        DayNo =Date[1]
       
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
            
        if(Style == 'D'):   
            print(YY,MM,DD,DayNo)
            print(EntT,EntLat,EntLng)
            print(ExtT,ExtLat,ExtLng)
        
        
        
