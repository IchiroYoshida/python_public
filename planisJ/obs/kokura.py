import ephem

obs = ephem.Observer()

obs.name = '小倉'
obs.lon = '130.8760'
obs.lat = '33.8826'
obs.date = '1955/09/11 21:00:00'
obs.date -= 9*ephem.hour
