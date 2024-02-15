import ephem

obs = ephem.Observer()

obs.name = '戸塚'
obs.lon = '139.534'
obs.lat = '35.401'
obs.date = '2023/10/19 3:30:00'
obs.date -= 9*ephem.hour
