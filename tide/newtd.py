"""
    New TD3 test!
    2023/06/16
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""
import func.td3 as td
import func.harm60 as h6

name = '石垣'
date = '2023/06/18'

td3 = td.TD3(name)
pt = h6.Tide(td3,date)

print(pt.ebb, pt.flow)
print(pt.tide)