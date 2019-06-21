import ephem

obs = ephem.Observer()

obs.name = '石垣'
obs.lon = '124.1640'
obs.lat = '24.3321'
obs.date = '2019/06/11 20:01:00'
obs.date -= 9*ephem.hour
