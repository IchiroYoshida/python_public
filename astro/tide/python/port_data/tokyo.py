import tide
"""
築地（東京）での潮位
"""
pt = tide.Port

pt.name = "築地H4"

pt.lat = 35.40
pt.lng =139.46
pt.level=120
pt.pl = [151.80,106.30,0.50,15.20,349.80,153.60,\
           0.00,166.60,0.00,193.30,0.00,181.00,76.60,\
         184.40,0.00,0.00,202.00,0.00,0.00,0.00,196.80,\
         158.30,177.00,0.00,162.40,0.00,163.50,198.50,\
         193.00,94.80,183.50,6.60,0.00,170.60,0.00,0.00,\
         145.40,165.20,208.70,0.00]

pt.hr = [9.80,3.60,1.60,2.60,1.10,4.00,0.00,18.60,0.00,0.60,\
         0.00,8.20,1.80,24.60,0.00,0.00,1.20,0.00,0.00,0.00,\
         1.50,7.30,2.60,0.00,50.10,0.00,2.20,1.80,23.90,0.20,\
         7.80,1.40,0.00,1.80,0.00,0.00,0.90,2.60,0.40,0.00]

pt.date = '2016/07/12'
pt.itv  = 20

today = tide.Tide(pt)

tt = today.tide(pt)

print (today.tl)
