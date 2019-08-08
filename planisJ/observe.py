import ephem

obs = ephem.Observer()

obs.name = '愛光学園'
obs.lon = '132.7332'
obs.lat = '33.8460'
obs.date = '2019/08/08 19:38:00'
obs.date -= 9*ephem.hour
