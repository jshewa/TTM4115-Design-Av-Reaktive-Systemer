function myMap() {
	var mapProp = {
		center: new google.maps.LatLng(63.419467, 10.393198),
		zoom: 17,
		mapTypeId: 'satellite'
	};
	var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

	var parentIcon = {
		url: 'images/parenticon.png',
		scaledSize: new google.maps.Size(25, 37),
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(12, 34)
	};
	var allgoodIcon = {
		url: 'images/allgoodicon.png',
		scaledSize: new google.maps.Size(25, 37),
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(12, 34)
	};
	var outsideIcon = {
		url: 'images/outofboundsicon.png',
		scaledSize: new google.maps.Size(25, 37),
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(12, 34)
	};
	var meetupIcon = {
		url: 'images/meetupicon.png',
		scaledSize: new google.maps.Size(25, 37),
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(12, 34)
	};

	var parentLatlng = new google.maps.LatLng(63.419093, 10.394088);
	var parentMarker = new google.maps.Marker({
		position: parentLatlng, animation: google.maps.Animation.DROP,
		icon: parentIcon
	});

	var childLatlng = new google.maps.LatLng(63.419092, 10.39402);
	var childMarker = new google.maps.Marker({
		position: childLatlng, animation: google.maps.Animation.DROP,
		icon: allgoodIcon
	});

	var allUL = new google.maps.LatLng(63.41991, 10.39232);
	var allUR = new google.maps.LatLng(63.420106, 10.39386);
	var allLR = new google.maps.LatLng(63.419016, 10.394405);
	var allLL = new google.maps.LatLng(63.418740, 10.3929);

	var allowedPolygonPath = [allUL, allUR, allLR, allLL];

	var allowedArea = new google.maps.Polygon({
		path: allowedPolygonPath,
		strokeColor: "#00D126",
		strokeOpacity: 0.55,
		strokeWeight: 4,
		fillColor: "#006745",
		fillOpacity: 0.12
	});

	if (navigator.geolocation) { // goes on the "parent marker"
		navigator.geolocation.getCurrentPosition(function (position) {
			parentLatlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude)
			parentMarker.position = parentLatlng
		}, function handleNoGeolocation(errorFlag) {
		});
	}

	allowedArea.setMap(map);
	parentMarker.setMap(map);
	childMarker.setMap(map);
};