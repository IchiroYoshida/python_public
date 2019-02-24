import ephem

obs = ephem.Observer()

obs.name = '愛光学園'
obs.lon = '132.7332'
obs.lat = '33.8460'
obs.date = '2018/09/01 21:00:00'
obs.date -= 9*ephem.hour
