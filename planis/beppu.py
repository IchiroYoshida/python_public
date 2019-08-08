import ephem

obs = ephem.Observer()

obs.name = '別府'
obs.lon = '131.495'
obs.lat = '33.277'
obs.date = '2019/01/23 18:50:00'
obs.date -= 9*ephem.hour
