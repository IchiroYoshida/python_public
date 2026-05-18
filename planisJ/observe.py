import ephem

obs = ephem.Observer()

obs.name = '福岡'
obs.lon = '130.387'
obs.lat = '33.594'
obs.date = '2026/01/20 03:00:00'
obs.date -= 9*ephem.hour
