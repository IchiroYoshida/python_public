"""
index.py
"""
class Index(object):
   def __init__(self,event):
       self.day_index  = ''
       self.day_object = ''
       self.day_event  = ''
   def day_event(self,event):
       self.day_index  = event.day_index
       self.day_object = event.day_object
       self.day_event  = event.day_event

day_event_dic  = {}

ix = Index()


