import simplekml
kml = simplekml.Kml()

ent = kml.newpoint()
ent.name ="Start"
ent.description = "2023-05-23 No.1 Entry point"
ent.coords = [(124.3490, 24.5653)]



lin = kml.newlinestring(name="Hirakubo drift diving",
          description="2023-05-23 No.1",
          coords =[(124.3490, 24.5653),     #Start lon,lat, 
                   (124.3571, 24.5836)])    #End
kml.save("skml1.kml")



