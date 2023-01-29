import ephem

obs = ephem.Observer()

obs.name = 'Fukuoka'
obs.lon = '130.387'
obs.lat = '33.594'
obs.date = '2023/01/28 20:00:00'
obs.date -= 9*ephem.hour

