/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng( 35.692900, 140.865300),5);

    var points1 = [
        new GLatLng( 20.000000, 131.986424),
        new GLatLng( 21.000000, 132.477131),
        new GLatLng( 22.000000, 132.975169),
        new GLatLng( 23.000000, 133.481055),
        new GLatLng( 24.000000, 133.995333),
        new GLatLng( 25.000000, 134.518582),
        new GLatLng( 26.000000, 135.051411),
        new GLatLng( 27.000000, 135.594472),
        new GLatLng( 28.000000, 136.148456),
        new GLatLng( 29.000000, 136.714102),
        new GLatLng( 30.000000, 137.292199),
        new GLatLng( 31.000000, 137.883594),
        new GLatLng( 32.000000, 138.489197),
        new GLatLng( 33.000000, 139.109985),
        new GLatLng( 34.000000, 139.747016),
        new GLatLng( 35.000000, 140.401431),
        new GLatLng( 36.000000, 141.074469),
        new GLatLng( 37.000000, 141.767477),
        new GLatLng( 38.000000, 142.481923),
        new GLatLng( 39.000000, 143.219409),
        new GLatLng( 40.000000, 143.981695),
        new GLatLng( 41.000000, 144.770713),
        new GLatLng( 42.000000, 145.588596),
        new GLatLng( 43.000000, 146.437704),
        new GLatLng( 44.000000, 147.320659),
        new GLatLng( 45.000000, 148.240386),
        new GLatLng( 46.000000, 149.200162),
    ];

    var line1 = new GPolyline(points1);

    map.addOverlay(line1);

  }
}
