/* Google Maps 東京スカイツリーの影 2015-12-6 16:00-16:15*/

function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById("map_canvas"));
    map.setCenter(new GLatLng(35.71004,139.8106),13);

    var points1 = [
	new GLatLng(35.71004,139.8106),
	new GLatLng(35.751077,139.893357),
	new GLatLng(35.760388,139.915234),
	new GLatLng(35.775887,139.951637),
	new GLatLng(35.71004,139.8106)
    ];

    var line1 = new GPolygon(points1);

    map.addOverlay(line1);

  }
}
