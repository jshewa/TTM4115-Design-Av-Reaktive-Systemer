(function () {
	function myMap() {
		var mapProp = {
			center: new google.maps.LatLng(63.419499, 10.402077),
			zoom: 16,
		};
		var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

		var myLatlng = new google.maps.LatLng(63.4195, 10.40206); //needs to be dynamic
		var marker = new google.maps.Marker({ position: myLatlng, animation: google.maps.Animation.DROP });

		var areaLatlng = new google.maps.LatLng(63.418, 10.402079); //could have this be static

		var allowedArea = new google.maps.Circle({
			center: areaLatlng,
			radius: 40,
			strokeColor: "#00FF33",
			strokeOpacity: 0.8,
			strokeWeight: 4,
			fillColor: "#0033FF",
			fillOpacity: 0.3
		});

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(function (position) {
				areaLatlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude)
				allowedArea.center = areaLatlng
			}, function handleNoGeolocation(errorFlag) {
				if (errorFlag == true) {
					alert("Geolocation service failed.");
				} else {
					alert("Your browser doesn't support geolocation.");
				}
			});
		}

		allowedArea.setMap(map);
		marker.setMap(map);

	}
})();