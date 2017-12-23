/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 132.048355),
        new GLatLng( 21.000000, 132.536555),
        new GLatLng( 22.000000, 133.031924),
        new GLatLng( 23.000000, 133.534969),
        new GLatLng( 24.000000, 134.046229),
        new GLatLng( 25.000000, 134.566273),
        new GLatLng( 26.000000, 135.095701),
        new GLatLng( 27.000000, 135.635155),
        new GLatLng( 28.000000, 136.185315),
        new GLatLng( 29.000000, 136.746908),
        new GLatLng( 30.000000, 137.320711),
        new GLatLng( 31.000000, 137.907554),
        new GLatLng( 32.000000, 138.508332),
        new GLatLng( 33.000000, 139.124005),
        new GLatLng( 34.000000, 139.755609),
        new GLatLng( 35.000000, 140.404266),
        new GLatLng( 36.000000, 141.071189),
        new GLatLng( 37.000000, 141.757698),
        new GLatLng( 38.000000, 142.465230),
        new GLatLng( 39.000000, 143.195355),
        new GLatLng( 40.000000, 143.949793),
        new GLatLng( 41.000000, 144.730432),
        new GLatLng( 42.000000, 145.539356),
        new GLatLng( 43.000000, 146.378868),
        new GLatLng( 44.000000, 147.251526),
        new GLatLng( 45.000000, 148.160180),
        new GLatLng( 46.000000, 149.108017),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
