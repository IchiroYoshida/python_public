/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 132.114722),
        new GLatLng( 21.000000, 132.600436),
        new GLatLng( 22.000000, 133.093156),
        new GLatLng( 23.000000, 133.593384),
        new GLatLng( 24.000000, 134.101649),
        new GLatLng( 25.000000, 134.618512),
        new GLatLng( 26.000000, 135.144567),
        new GLatLng( 27.000000, 135.680442),
        new GLatLng( 28.000000, 136.226809),
        new GLatLng( 29.000000, 136.784382),
        new GLatLng( 30.000000, 137.353924),
        new GLatLng( 31.000000, 137.936253),
        new GLatLng( 32.000000, 138.532247),
        new GLatLng( 33.000000, 139.142849),
        new GLatLng( 34.000000, 139.769075),
        new GLatLng( 35.000000, 140.412026),
        new GLatLng( 36.000000, 141.072891),
        new GLatLng( 37.000000, 141.752964),
        new GLatLng( 38.000000, 142.453652),
        new GLatLng( 39.000000, 143.176491),
        new GLatLng( 40.000000, 143.923164),
        new GLatLng( 41.000000, 144.695517),
        new GLatLng( 42.000000, 145.495586),
        new GLatLng( 43.000000, 146.325619),
        new GLatLng( 44.000000, 147.188110),
        new GLatLng( 45.000000, 148.085836),
        new GLatLng( 46.000000, 149.021901),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
