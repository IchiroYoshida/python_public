class DayEvent(object):
    def day(self,event):
        self.index = event.index
        self.tname = event.tname
        self.mage  = event.mage
        self.moon_rise = event.moon_rise
        self.moon_set  = event.moon_set
        self.sun_rise  = event.sun_rise
        self.sun_set   = event.sun_set

day1= DayEvent()

day1.index = '160701'
day1.tname = '中潮'
day1.mage  = 26.0
day1.moon_rise = '01:37:28'
day1.moon_set  = '15:25:54'

