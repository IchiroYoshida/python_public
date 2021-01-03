import ephem

obs = ephem.Observer()

obs.name = '那覇'
obs.lon = '127.678'
obs.lat = '26.213'
obs.date = '2019/01/22 18:07:00'
obs.date -= 9*ephem.hour
