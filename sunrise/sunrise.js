/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 122.053304),
        new GLatLng( 21.000000, 122.543957),
        new GLatLng( 22.000000, 123.041940),
        new GLatLng( 23.000000, 123.547770),
        new GLatLng( 24.000000, 124.061992),
        new GLatLng( 25.000000, 124.585183),
        new GLatLng( 26.000000, 125.117953),
        new GLatLng( 27.000000, 125.660953),
        new GLatLng( 28.000000, 126.214875),
        new GLatLng( 29.000000, 126.780457),
        new GLatLng( 30.000000, 127.358488),
        new GLatLng( 31.000000, 127.949816),
        new GLatLng( 32.000000, 128.555349),
        new GLatLng( 33.000000, 129.176066),
        new GLatLng( 34.000000, 129.813023),
        new GLatLng( 35.000000, 130.467362),
        new GLatLng( 36.000000, 131.140321),
        new GLatLng( 37.000000, 131.833247),
        new GLatLng( 38.000000, 132.547607),
        new GLatLng( 39.000000, 133.285005),
        new GLatLng( 40.000000, 134.047198),
        new GLatLng( 41.000000, 134.836119),
        new GLatLng( 42.000000, 135.653900),
        new GLatLng( 43.000000, 136.502901),
        new GLatLng( 44.000000, 137.385744),
        new GLatLng( 45.000000, 138.305353),
        new GLatLng( 46.000000, 139.265002),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
