"""
    New TD3 test!
    2023/06/16
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""
import func.td3 as td
import func.harm60 as h6
import func.MoonEph as ME

name = '石垣'
date = '2023/06/20'

td3 = td.TD3(name)
pt = h6.Tide(td3,date)
me = ME.MoonEph(date)

print(pt.ebb, pt.flow)
print(pt.tide)
print(me.tide_name)
print(me.moon_age)

