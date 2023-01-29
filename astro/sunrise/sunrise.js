/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 132.115856),
        new GLatLng( 21.000000, 132.601416),
        new GLatLng( 22.000000, 133.093972),
        new GLatLng( 23.000000, 133.594025),
        new GLatLng( 24.000000, 134.102105),
        new GLatLng( 25.000000, 134.618772),
        new GLatLng( 26.000000, 135.144617),
        new GLatLng( 27.000000, 135.680271),
        new GLatLng( 28.000000, 136.226403),
        new GLatLng( 29.000000, 136.783727),
        new GLatLng( 30.000000, 137.353006),
        new GLatLng( 31.000000, 137.935055),
        new GLatLng( 32.000000, 138.530753),
        new GLatLng( 33.000000, 139.141041),
        new GLatLng( 34.000000, 139.766934),
        new GLatLng( 35.000000, 140.409532),
        new GLatLng( 36.000000, 141.070023),
        new GLatLng( 37.000000, 141.749698),
        new GLatLng( 38.000000, 142.449962),
        new GLatLng( 39.000000, 143.172351),
        new GLatLng( 40.000000, 143.918544),
        new GLatLng( 41.000000, 144.690385),
        new GLatLng( 42.000000, 145.489907),
        new GLatLng( 43.000000, 146.319354),
        new GLatLng( 44.000000, 147.181217),
        new GLatLng( 45.000000, 148.078268),
        new GLatLng( 46.000000, 149.013607),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
