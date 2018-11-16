//function initMap()
//{
//}
//window.onload = function()
//{
	var map;
	var infoWindow;

	var mapUrl = "map";
	var cultureUrl = "culture";
	var seedUrl = "seed";

	var mapData;
	var cultureData;
	var seedData;

	var fieldDetail = "";

	function initMap()
	{
		let cultureRequest = new XMLHttpRequest();
		cultureRequest.open("GET", cultureUrl);
		cultureRequest.onload = function()
		{
			cultureData = JSON.parse(cultureRequest.responseText);
		}
		cultureRequest.send();

		let seedRequest = new XMLHttpRequest();
		seedRequest.open("GET", seedUrl);
		seedRequest.onload = function()
		{
			seedData = JSON.parse(seedRequest.responseText);
		}
		seedRequest.send();

		let mapRequest = new XMLHttpRequest();
		mapRequest.open("GET", mapUrl);
		mapRequest.onload = function()
		{
			mapData = JSON.parse(mapRequest.responseText);
			//cultureData[seedData[i].culture -1].color
			//console.log(cu);
			for(let i = 0; i < seedData.length; i++)
			{
				DrawField(map, showArrays, cultureData[seedData[i].culture -1].color, JSON.parse(mapData[seedData[i].field-1].polygon), i);
			}
		}
		mapRequest.send();

		let options = {
			zoom:18,
			center:{lat:49.327839, lng:31.518580}
		}

		map = new google.maps.Map(document.getElementById('map'), options);
		infoWindow = new google.maps.InfoWindow;


		var isClosed = false;
    var poly = new google.maps.Polyline({ map: map, path: [], strokeColor: "#FF0000", strokeOpacity: 1.0, strokeWeight: 2 });
    google.maps.event.addListener(map, 'click', function (clickEvent) {
        if (isClosed)
            return;
        var markerIndex = poly.getPath().length;
        var isFirstMarker = markerIndex === 0;
        var marker = new google.maps.Marker({ map: map, position: clickEvent.latLng, draggable: true });
        if (isFirstMarker) {
            google.maps.event.addListener(marker, 'click', function () {
                if (isClosed)
                    return;
                var path = poly.getPath();
                poly.setMap(null);
                poly = new google.maps.Polygon({ map: map, path: path, strokeColor: "#FF0000", strokeOpacity: 0.8, strokeWeight: 2, fillColor: "#FF0000", fillOpacity: 0.35 });
                isClosed = true;
            });
        }
        google.maps.event.addListener(marker, 'drag', function (dragEvent) {
            poly.getPath().setAt(markerIndex, dragEvent.latLng);
        });
        poly.getPath().push(clickEvent.latLng);
    });
	}

	[{"lat": 49.327250, "lng": 31.518933},{"lat": 49.327394, "lng": 31.519160},{"lat": 49.327691, "lng": 31.519306},{"lat": 49.327286, "lng": 31.519880},{"lat": 49.326884, "lng": 31.519403},{"lat": 49.327250, "lng": 31.518933}]

	function DrawField(map, fieldDetailFunc, color, coords, id)
	{
		let fieldTriangle = new google.maps.Polygon({
		      	paths: coords,
		      	strokeColor: color,
		      	strokeOpacity: 0.8,
		      	strokeWeight: 2,
		      	fillColor: color,
		      	fillOpacity: 0.35
	    });
	    fieldTriangle.setMap(map);
	    fieldDetail = "<p></p>";
	    fieldTriangle.addListener('click', fieldDetailFunc);
	}

	function showArrays(event)
	{
	    // Replace the info window's content and position.
	    infoWindow.setContent(fieldDetail);
	    infoWindow.setPosition(event.latLng);

	    infoWindow.open(map);
		}

		var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	    acc[i].addEventListener("click", function() {
	        this.classList.toggle("active");
	        var panel = this.nextElementSibling;
	        if (panel.style.display === "block") {
	            panel.style.display = "none";
	        } else {
	            panel.style.display = "block";
	        }
	    });
	}
//}