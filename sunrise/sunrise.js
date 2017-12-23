/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 131.985590),
        new GLatLng( 21.000000, 132.476296),
        new GLatLng( 22.000000, 132.974334),
        new GLatLng( 23.000000, 133.480220),
        new GLatLng( 24.000000, 133.994498),
        new GLatLng( 25.000000, 134.517747),
        new GLatLng( 26.000000, 135.050576),
        new GLatLng( 27.000000, 135.593637),
        new GLatLng( 28.000000, 136.147621),
        new GLatLng( 29.000000, 136.713267),
        new GLatLng( 30.000000, 137.291364),
        new GLatLng( 31.000000, 137.882759),
        new GLatLng( 32.000000, 138.488362),
        new GLatLng( 33.000000, 139.109150),
        new GLatLng( 34.000000, 139.746181),
        new GLatLng( 35.000000, 140.400596),
        new GLatLng( 36.000000, 141.073634),
        new GLatLng( 37.000000, 141.766642),
        new GLatLng( 38.000000, 142.481087),
        new GLatLng( 39.000000, 143.218574),
        new GLatLng( 40.000000, 143.980859),
        new GLatLng( 41.000000, 144.769877),
        new GLatLng( 42.000000, 145.587760),
        new GLatLng( 43.000000, 146.436868),
        new GLatLng( 44.000000, 147.319823),
        new GLatLng( 45.000000, 148.239551),
        new GLatLng( 46.000000, 149.199327),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
