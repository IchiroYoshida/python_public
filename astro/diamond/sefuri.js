/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng(33.436599,130.36837),13);

    var points1 = [
        new GLatLng(33.436599,130.36837),
        new GLatLng(33.2429534159,130.809417195),
        new GLatLng(33.2734107549,130.80508012),
        new GLatLng(33.347771772,130.79726781),
        new GLatLng(33.4351286293,130.793194259),
        new GLatLng(33.5217571826,130.79533435),
        new GLatLng(33.603156932,130.802346124),
        new GLatLng(33.6409783507,130.807112421),
        new GLatLng(33.436599,130.36837)
    ];

    var line1 = new GPolygon(points1);

    map.addOverlay(line1);

  }
}
