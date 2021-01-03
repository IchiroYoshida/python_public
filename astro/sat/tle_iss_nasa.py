#! /usr/local/bin/python3.6
"""
TLEs data from NASA

"""
from datetime import datetime
from datetime import timedelta
import re
import requests
import sys
import traceback

#FILE ='./iss_tle.py'

class TleIssNasa:
    URL = (
        "https://spaceflight.nasa.gov/realdata/sightings/"
        "SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html"
    )
    UA = (
        "mk-mode Bot (by Python/{}.{}.{}, "
        "Administrator: postmaster@mk-mode.com)"
    ).format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro
    )
    MSG_ERR = (
        "Invalid date!\n"
    )

    def __init__(self):
        if len(sys.argv) < 2:
            self.jst = datetime.now()
        else:
            if re.search(r"^(\d{8}|\d{14})$", sys.argv[1]) is not(None):
                dt = sys.argv[1].ljust(14, "0")
                try:
                    self.jst = datetime.strptime(dt, "%Y%m%d%H%M%S")
                except ValueError as e:
                    print(self.MSG_ERR)
                    sys.exit(1)
            else:
                print(self.MSG_ERR)
                sys.exit(0)
        self.utc = self.jst - timedelta(hours=9)

    def exec(self):
        """ Execution """
        tle = ""
        utc_tle = None
        try:
            #print(self.jst.strftime("%Y-%m-%d %H:%M:%S.%f JST"))
            #print(self.utc.strftime("%Y-%m-%d %H:%M:%S.%f UTC"))
            #print("---")
            tles = self.__get_tle()
            return(tles)
            """
            tle_sets = []

            for new in reversed(tles):
                tle = new
                item_utc = re.split(" +", tle[0])[3]
                y = 2000 + int(item_utc[0:2])
                d = float(item_utc[2:])-1
                utc_tle = datetime(y, 1, 1) + timedelta(days=d)
                tle_sets.append([utc_tle, tle[0], tle[1]])

                if utc_tle <= self.utc + timedelta(days=1):
                    break
            #print("\n".join(tle))
            #print(utc_tle.strftime("(%Y-%m-%d %H:%M:%S.%f UTC)"))
            return(tle_sets)
            """

        except Exception as e:
            raise

    def __get_tle(self):
        """ 最新 TLE 一覧取得 """
        res = []
        try:
            html, status, reason = self.__get_html()
            if status != 200 or reason != "OK":
                print((
                    "STATUS: {} ({})"
                    "[ERROR] Could not retreive html."
                ).format(status, reason))
                sys.exit(1)
            for tle in re.findall(r"ISS\n +(1.+?)\n +(2.+?)\n", html):
                res.append([tle[0], tle[1]])
            return res
        except Exception as e:
            raise

    def __get_html(self):
        """ HTML 取得 """
        try:
            headers = {'User-Agent': self.UA}
            res = requests.get(self.URL, headers)
            return [res.text, res.status_code, res.reason]
        except Exception as e:
            raise

def tle_utc(utc, tles):
    delta_tle = []

    #obj = TleIssNasa()
    #tles = obj.exec()
    
    for tle in tles:
        item_utc = re.split(" +", tle[0])[3]
        y = 2000 + int(item_utc[0:2])
        d = float(item_utc[2:])-1
        utc_tle = datetime(y, 1, 1) + timedelta(days=d)

        delta = utc - utc_tle
        delta2 = abs(float(delta.total_seconds()))
        delta_tle.append([delta2, tle])
    tle_min = min(delta_tle, key = lambda x:x[0])
    del tle_min[0]
    return(tle_min[0])


if __name__ == '__main__':
    try:
        obj = TleIssNasa()
        tle = obj.exec()
        print('TLE = ',tle)

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
