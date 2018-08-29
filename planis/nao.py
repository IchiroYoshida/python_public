import ephem

obs = ephem.Observer()

obs.name = '直島'
obs.lon = '133.9750'
obs.lat = '34.4597'
obs.date = '2018/09/13 19:00:00'
obs.date -= 9*ephem.hour
