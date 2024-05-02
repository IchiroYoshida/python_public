'''
ISS TLE from NORAD
2024-04-40 
'''
from skyfield.api import load, wgs84

stations_url = 'https://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

by_name = {sat.name: sat for sat in satellites}
satellite = by_name['ISS (ZARYA)']
print(satellite)

sgp4_model = satellite.model

print("衛星名: ", satellite.name)
print("元期: ", satellite.epoch.utc_jpl())
print("衛星番号: ", sgp4_model.satnum)
print("エポック年: ", sgp4_model.epochyr)
print("エポック日: ", sgp4_model.epochdays)
print("エポックのユリウス日: ", sgp4_model.jdsatepoch)
print("ndot: ", sgp4_model.ndot)
print("nddot: ", sgp4_model.nddot)
print("弾道抗力係数 B*: ", sgp4_model.bstar)
print("軌道傾斜角[rad]: ", sgp4_model.inclo)
print("昇交点赤経[rad]: ", sgp4_model.nodeo)
print("離心率: ", sgp4_model.ecco)
print("近地点引数[rad]: ", sgp4_model.argpo)
print("平均近点角[rad]: ", sgp4_model.mo)
print("平均運動[rad/min]: ", sgp4_model.no_kozai)
