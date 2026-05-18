import ephem

obs = ephem.Observer()

obs.name = 'Fukuoka'
obs.lon = '130.387'
obs.lat = '33.594'
obs.date = '2026/01/20 0:00:00'
obs.date -= 9*ephem.hour
