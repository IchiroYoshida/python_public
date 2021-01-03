/* Google Maps PrnJavaScript */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng(35.689213,139.691787),13);

    var points1 = [
        new GLatLng(35.689213,139.691787),
        new GLatLng(35.7135346396,139.762043385),
        new GLatLng(35.7138635604,139.763078794),
        new GLatLng(35.7142019046,139.764143941),
        new GLatLng(35.7145501097,139.765240101),
        new GLatLng(35.7149085464,139.766368655),
        new GLatLng(35.7152777598,139.767531004),
        new GLatLng(35.7156581461,139.76872872),
        new GLatLng(35.7160502739,139.769963382),
        new GLatLng(35.7164546594,139.771236727),
        new GLatLng(35.7168718809,139.772550582),
        new GLatLng(35.7173025553,139.773906896),
        new GLatLng(35.7177473652,139.775307707),
        new GLatLng(35.7182069828,139.776755251),
        new GLatLng(35.7186821482,139.778251868),
        new GLatLng(35.7191736912,139.779800054),
        new GLatLng(35.689213,139.691787)
    ];

    var line1 = new GPolygon(points1);

    map.addOverlay(line1);

  }
}
