(function () {
	//also map center
	var parentLatlng = new google.maps.LatLng(63.419093, 10.394088);
	var doubleClicked = false;
	var mapProp = {
		center: new google.maps.LatLng(63.419467, 10.393198), //63.419467, 10.393198 <- park center
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

	var parentMarker = new SlidingMarker({
		position: parentLatlng, animation: google.maps.Animation.DROP,
		icon: parentIcon,
		duration: 7500
	});
	parentMarker.setEasing(null);
	var backInParentLatlng = new google.maps.LatLng(63.41903, 10.39423);
	parentMarker.addListener('click', function () {
		if (meetingUp) {
			parentMarker.setPosition(backInParentLatlng);
		}
	});
	parentMarker.addListener('dblclick', function () {
		map.setCenter(parentMarker.position);
		childCenter = false;
	});


	var outsideLatlng = new google.maps.LatLng(63.418967, 10.394368);
	var backInLatlng = new google.maps.LatLng(63.419023, 10.394252);
	var meetupLatlng = new google.maps.LatLng(63.419025, 10.39425);
	var aftermeetupLatlng = new google.maps.LatLng(63.419024, 10.39424);
	var childLatlng = new google.maps.LatLng(63.419092, 10.39406);
	var childClickCount = 0;
	var meetingUp = false;
	var childCenter = false;
	var childMarker = new SlidingMarker({
		position: childLatlng, animation: google.maps.Animation.DROP,
		icon: allgoodIcon,
		duration: 8000,
	});
	childMarker.setEasing(null);
	childMarker.addListener('dblclick', function () {
		doubleClicked = true;
		map.setCenter(childMarker.getAnimationPosition());
		childCenter = true;
	});

	var handleChildSingleClick = function () {
		if (!doubleClicked) {
			if (childClickCount == 0) {
				childMarker.setPosition(outsideLatlng);
			}
			if (childClickCount == 1) {
				childMarker.setPosition(backInLatlng);
			}
			if (childClickCount == 2) {
				childMarker.setDuration(2500);
				childMarker.setPosition(meetupLatlng);
				meetingUp = true;
			}
			if (childClickCount == 3) {
				window.setTimeout(childMarker.setPosition(aftermeetupLatlng), 1000);
			}
			childClickCount += 1;
		}
	};

	childMarker.addListener('click', function () {
		doubleClicked = false;
		window.setTimeout(handleChildSingleClick, 350);
	}, false);
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

	childMarker.addListener('animationposition_changed', function () {
		if (childCenter) {
			map.setCenter(childMarker.getAnimationPosition());
		}
		var icon =
			google.maps.geometry.poly.containsLocation(childMarker.getAnimationPosition(), allowedArea) ?
			allgoodIcon : outsideIcon;
		childMarker.setIcon(icon);
		if (childMarker.getAnimationPosition() == meetupLatlng) {
			childMarker.setIcon(meetupIcon);
		}
		if (childMarker.getAnimationPosition() == aftermeetupLatlng) {
			childMarker.setIcon(allgoodIcon);
		}
	}, false);

	parentMarker.addListener('animationposition_changed', function () {
		map.setCenter(parentMarker.getAnimationPosition());
	});

	allowedArea.setMap(map);
	parentMarker.setMap(map);
	childMarker.setMap(map);
})();