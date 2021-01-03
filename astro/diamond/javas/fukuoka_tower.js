/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng(33.593305,130.351485),13);

    var points1 = [
        new GLatLng(33.593305,130.351485),
        new GLatLng(33.5678576269,130.411118112),
        new GLatLng(33.5718900372,130.410643518),
        new GLatLng(33.5818489118,130.409757695),
        new GLatLng(33.593685671,130.409221672),
        new GLatLng(33.6054626422,130.409312629),
        new GLatLng(33.6164598956,130.409898968),
        new GLatLng(33.6215242302,130.41032191),
        new GLatLng(33.593305,130.351485)
    ];

    var line1 = new GPolygon(points1);

    map.addOverlay(line1);

  }
}
