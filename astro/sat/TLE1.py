"""
  TLE data of ISS
  2021-12-12 Ichiro
 """
import requests
import sys
import traceback
    
URL = "http://celestrak.com/NORAD/elements/stations.txt"


def TleISS():  
      res = requests.get(URL)
      html = res.text.splitlines()

      tle = []

      for i in range(3):
            tle.append(html[i])
      return(tle)

if __name__ == '__main__':
      try:
            tle = TleISS()
            print('TLE =',tle)
            
      except Exception as e:
            traceback.print_exc()
            sys.exit(1)
              