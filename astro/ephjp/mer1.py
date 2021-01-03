import ephem

RAD = 180. / ephem.pi

fuk = ephem.Observer()
fuk.lon = '130.391'
fuk.lat = '33.593'
fuk.elevation = 20
fuk.date = '2018/12/3 19:30'
fuk.pressure = 0
fuk.horizon = '-0:34'

v = ephem.Venus(fuk)
m = ephem.Moon(fuk)

s = ephem.separation(v, m) * RAD

print ("Moon and Venus angle %f" % s)


