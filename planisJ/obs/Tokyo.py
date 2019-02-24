import ephem

obs = ephem.Observer()

obs.name = '東京'
obs.lon = '139.6010'
obs.lat = '35.6694'
obs.date = '2019/02/25 5:05:00'
obs.date -= 9*ephem.hour
