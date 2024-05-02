'''
ISS TLE from NORAD
2024-04-30
'''
import requests

URL = 'https://celestrak.org/NORAD/elements/stations.txt'

tle = requests.get(URL).text.split('\r\n')[0:3]
print(tle)
