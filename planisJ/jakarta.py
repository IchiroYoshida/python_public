import ephem

obs = ephem.Observer()

obs.name = 'Jakarta'
obs.lon = '106.7555'
obs.lat = '-6.1059'
obs.date = '2018/9/17 20:32:00'
obs.date -= 9*ephem.hour
