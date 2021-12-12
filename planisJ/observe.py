import ephem

obs = ephem.Observer()

obs.name = '福岡'
obs.lon = '130.390'
obs.lat = '33.593'
obs.date = '2021/12/11 20:00:00'
obs.date -= 9*ephem.hour
