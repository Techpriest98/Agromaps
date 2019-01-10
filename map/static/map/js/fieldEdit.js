	var map;
	var mapUrl = "map";

	document.getElementById('toggle-btn').onclick = function()
	{
		document.getElementById('sidebar-wrapper').classList.toggle('active');
		document.getElementById('toggle-btn').classList.toggle('active');
	}

	function initMap()
	{
		let mapRequest = new XMLHttpRequest();

		let mapData;

		mapRequest.open("GET", mapUrl);
		mapRequest.onload = function()
		{
			mapData = JSON.parse(mapRequest.responseText);
			//console.log(cu);
			for(let i = 0; i < mapData.length; i++)
			{
				fields = mapData;
				DrawField(map, showArrays, "#000", mapData[i], i);
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
       	{
            return;
       	}
        var markerIndex = poly.getPath().length;
        var isFirstMarker = markerIndex === 0;
        var marker = new google.maps.Marker({ map: map, position: clickEvent.latLng, draggable: true });
        if (isFirstMarker) {
            google.maps.event.addListener(marker, 'click', function () {
                if (isClosed || poly.getPath().length < 3)
                    return;
                var path = poly.getPath();
                poly.setMap(null);
                poly = new google.maps.Polygon({ map: map, path: path, strokeColor: "#FF0000", strokeOpacity: 0.8, strokeWeight: 2, fillColor: "#FF0000", fillOpacity: 0.35 });
                document.getElementsByName('polygon')[0].value = JSON.stringify(poly.getPath().j);
                isClosed = true;
            });
        }
        google.maps.event.addListener(marker, 'drag', function (dragEvent) {
            poly.getPath().setAt(markerIndex, dragEvent.latLng);
            if(isClosed)
            document.getElementsByName('polygon')[0].value = JSON.stringify(poly.getPath().j);
        });
        poly.getPath().push(marker.position);
    });
	}

	function DrawField(map, fieldDetailFunc, color, field, id)
	{
		let fieldTriangle = new google.maps.Polygon({
		      	paths: JSON.parse(field.polygon),
		      	strokeColor: color,
		      	strokeOpacity: 0.8,
		      	strokeWeight: 2,
		      	fillColor: color,
		      	fillOpacity: 0.35
	    });
	    fieldTriangle.setMap(map);
	    fieldTriangle.addListener('click', function(event){
	    	showArrays(event, field)
	    });
	}

	function showArrays(event, field)
	{
	    // Replace the info window's content and position.
	    infoWindow.setContent("<h6>"+field.title+"<h6>");
	    infoWindow.setPosition(event.latLng);

	    infoWindow.open(map);
	}