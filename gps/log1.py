'''
Yaeyama Diving Logs -> Google Eartrh kml
2023-05-23
'''
import simplekml

class DLogKml:
    #Anchoring Log
    Anchor = simplekml.Style()
    Anchor.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/shapes/sailing.png'
    Anchor.labelstyle.scale = 0.66
    #Drift Log, Entry
    EntryPoint = simplekml.Style()
    EntryPoint.iconstyle.icon.href ='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'
    EntryPoint.labelstyle.scale = 0.66
    #Drift Log, Exit
    ExitPoint = simplekml.Style()
    ExitPoint.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/pink-blank.png'
    ExitPoint.labelstyle.scale = 0.66

    def anchor_plot(self, lnglat, description):
        pnt = self.kml.newpoint(name = description, coords=[lnglat])
        pnt.style = Anchor

    def drift_plot(self, lnglats, descriptions):
        if descriptions is None:
            descriptions = [''] * len(lnglats)
        else:
            assert len(lnglats) == len(descriptions)

        pnt = self.kml.newpoint(name="Entry: "+ description,coords=[lnglats[0]]) 

        for idx, (lnglat, description) in enumerate(zip(lnglats, descriptions)):
            pnt = self.kml.newpoint(coords=[lnglat])
 
        if linestring:
            ls = self.kml.newlinestring(name='LineString', coords=lnglats)
            ls.style = self.STYLE_LS
 
    def save(self, path):
        self.kml.save(path)
 