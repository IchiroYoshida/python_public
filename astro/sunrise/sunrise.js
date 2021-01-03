/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 132.115862),
        new GLatLng( 21.000000, 132.601422),
        new GLatLng( 22.000000, 133.093978),
        new GLatLng( 23.000000, 133.594031),
        new GLatLng( 24.000000, 134.102111),
        new GLatLng( 25.000000, 134.618777),
        new GLatLng( 26.000000, 135.144622),
        new GLatLng( 27.000000, 135.680276),
        new GLatLng( 28.000000, 136.226408),
        new GLatLng( 29.000000, 136.783732),
        new GLatLng( 30.000000, 137.353011),
        new GLatLng( 31.000000, 137.935061),
        new GLatLng( 32.000000, 138.530758),
        new GLatLng( 33.000000, 139.141046),
        new GLatLng( 34.000000, 139.766940),
        new GLatLng( 35.000000, 140.409537),
        new GLatLng( 36.000000, 141.070028),
        new GLatLng( 37.000000, 141.749703),
        new GLatLng( 38.000000, 142.449967),
        new GLatLng( 39.000000, 143.172356),
        new GLatLng( 40.000000, 143.918549),
        new GLatLng( 41.000000, 144.690390),
        new GLatLng( 42.000000, 145.489912),
        new GLatLng( 43.000000, 146.319359),
        new GLatLng( 44.000000, 147.181222),
        new GLatLng( 45.000000, 148.078273),
        new GLatLng( 46.000000, 149.013613),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
