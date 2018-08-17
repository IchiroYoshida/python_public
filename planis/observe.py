import ephem

obs = ephem.Observer()

obs.name = '福岡'
obs.lon = '130.390'
obs.lat = '33.593'
obs.date = '28701/06/01 00:00:00'
obs.date -= 9*ephem.hour
