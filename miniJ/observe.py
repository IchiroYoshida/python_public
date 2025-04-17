import ephem

obs = ephem.Observer()

obs.name = '福岡'
obs.lon = '130.387'
obs.lat = '33.594'
obs.date = '2025/04/17 20:00:00'
obs.date -= 9*ephem.hour
