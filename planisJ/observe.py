import ephem

obs = ephem.Observer()

obs.name = '久万高原天文台'
obs.lon = '132.941'
obs.lat = '33.678'
obs.elevation = 600
obs.date = '2021/04/20 20:00:00'
obs.date -= 9*ephem.hour
