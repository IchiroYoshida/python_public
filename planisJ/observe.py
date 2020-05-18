import ephem

obs = ephem.Observer()

obs.name = '東京'
obs.lon = '139.6010'
obs.lat = '35.6694'
obs.date = '2020/05/16 21:00:00'
obs.date -= 9*ephem.hour
