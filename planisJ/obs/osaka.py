import ephem

obs = ephem.Observer()

obs.name = '大阪'
obs.lon = '135.50'
obs.lat = '34.69'
obs.date = '2019/02/25 5:08:00'
obs.date -= 9*ephem.hour
