(function () {
	function myMap() {
		var mapProp = {
			center: new google.maps.LatLng(63.419499, 10.402077),
			zoom: 14,
		};
		var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
	}
})();