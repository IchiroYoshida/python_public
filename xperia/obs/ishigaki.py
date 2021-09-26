import ephem

obs = ephem.Observer()

obs.name = '石垣'
obs.lon = '124.1640'
obs.lat = '24.3321'
obs.date = '2018/09/01 21:00:00'
obs.date -= 9*ephem.hour
