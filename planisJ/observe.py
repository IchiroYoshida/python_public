import ephem

obs = ephem.Observer()

obs.name = '福岡'
obs.lon = '130.390'
obs.lat = '33.593'
obs.date = '2019/03/21 19:07:00'
obs.date -= 9*ephem.hour
