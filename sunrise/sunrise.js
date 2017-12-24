/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 131.973926),
        new GLatLng( 21.000000, 132.464632),
        new GLatLng( 22.000000, 132.962670),
        new GLatLng( 23.000000, 133.468556),
        new GLatLng( 24.000000, 133.982834),
        new GLatLng( 25.000000, 134.506082),
        new GLatLng( 26.000000, 135.038912),
        new GLatLng( 27.000000, 135.581973),
        new GLatLng( 28.000000, 136.135956),
        new GLatLng( 29.000000, 136.701602),
        new GLatLng( 30.000000, 137.279699),
        new GLatLng( 31.000000, 137.871094),
        new GLatLng( 32.000000, 138.476697),
        new GLatLng( 33.000000, 139.097485),
        new GLatLng( 34.000000, 139.734516),
        new GLatLng( 35.000000, 140.388931),
        new GLatLng( 36.000000, 141.061969),
        new GLatLng( 37.000000, 141.754977),
        new GLatLng( 38.000000, 142.469422),
        new GLatLng( 39.000000, 143.206908),
        new GLatLng( 40.000000, 143.969194),
        new GLatLng( 41.000000, 144.758212),
        new GLatLng( 42.000000, 145.576094),
        new GLatLng( 43.000000, 146.425202),
        new GLatLng( 44.000000, 147.308157),
        new GLatLng( 45.000000, 148.227885),
        new GLatLng( 46.000000, 149.187660),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
