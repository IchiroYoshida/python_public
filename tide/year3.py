'''
潮時表
2023/06/24
Ichiro Yoshida (yoshida.ichi@gmail.com)
'''

from datetime import datetime
import pandas as pd
import func.td3 as td
import func.harm60 as h6
import func.MoonEph as ME

name = '石垣'
year = '2023'

def strtimlev(time, level):
    tim = time.to_pydatetime().strftime('%H:%M ')
    lev = '{:>3.0f} '.format(level)
    return tim, lev

td3 = td.TD3(name)

days = pd.date_range(start=year+'-01-01', end=year+'-12-31', freq = 'D')

for months in range(7,9):
    print(name, year, months)
    print('  日    月齢       満潮  (cm)               干潮  (cm)       ')
    
    month = days[days.month == months]
    for day in month:
        date = day.to_pydatetime().strftime('%Y/%m/%d')
        dd   = day.to_pydatetime().day
        d2   = '{:>2d}'.format(dd)
        
        pt = h6.Tide(td3,date)
        me = ME.MoonEph(date)
        
        weekday = ME.WeekDay(date)
        ebbs_level = pt.ebb.values.tolist()
        ebbs_time  = pt.ebb.index.tolist()
        flows_level = pt.flow.values.tolist()
        flows_time = pt.flow.index.tolist()
        
        timE1, levE1 = '', ''
        timE2, levE2 = '', '' 
        timF1, levF1 = '', ''
        timF2, levF2 = '', '' 
     
        num = len(ebbs_time)
        if (num == 2):
            timE1, levE1 = strtimlev(ebbs_time[0], ebbs_level[0])
            timE2, levE2 = strtimlev(ebbs_time[1], ebbs_level[1])
        elif (num == 1):
            timE1, levE1 = strtimlev(ebbs_time[0], ebbs_level[0])
            timE2, levE2 = '**:**', ' --- ' 
        else :
            timE1, levE1 = '**:**', ' --- '
            timE2, levE2 = '**:**', ' --- '
                   
        num = len(flows_time)
        if (num == 2):
            timF1, levF1 = strtimlev(flows_time[0], flows_level[0])
            timF2, levF2 = strtimlev(flows_time[1], flows_level[1])
        elif (num == 1):
            timF1, levF1 = strtimlev(flows_time[0], flows_level[0])
            timF2, levF2 = '**:**', ' --- '
        else :
            timF1, levF1 = '**:**', ' --- '
            timF2, levF2 = '**:**', ' --- '
                   
        MoonAge = '{:>4}'.format(me.moon_age)
        prn_ephem = '{0} {1}  {2} {3} '.format(d2,weekday,me.tide_name,MoonAge)
        prn_ebbflow = timF1+'-'+levF1+' '+timF2+'-'+levF2+'  ' \
                    + timE1+'-'+levE1+' '+timE2+'-'+levE2
        prn_line = prn_ephem + prn_ebbflow
                    
        print(prn_line)
