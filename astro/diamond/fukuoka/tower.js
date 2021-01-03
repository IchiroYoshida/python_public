/* Google Maps PrnJavaScript */
function initialize() {
   if (GBrowserIsCompatible()){
       var map = new GMap2(document.getElementById("map_canvas"));
       map.setCenter(new GLatLng(33.593312, 130.351472),13);
       var points1 = [
        new GLatLng(33.593312,130.351472),
        new GLatLng(33.58826315748987,130.3863085016299),
        new GLatLng(33.593312,130.351472)
    ];

    var line1 = new GPolygon(points1);

    map.addOverlay(line1);

  }
}
