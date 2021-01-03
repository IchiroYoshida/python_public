/* Google Maps Shadow of Fukuoka Tower 2016 */
function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng(33.593305,130.351485),13);

    var points1 = [
	new GLatLng(33.593305,130.351485),
	new GLatLng(33.579929,130.382831),
	new GLatLng(33.582048,130.382581),
	new GLatLng(33.587283,130.382116),
	new GLatLng(33.593505,130.381834),
	new GLatLng(33.599696,130.381882),
	new GLatLng(33.605476,130.382190),
	new GLatLng(33.608138,130.382412),
	new GLatLng(33.593305,130.351485)
    ];

    var line1 = new GPolygon(points1);

    map.addOverlay(line1);

  }
}
