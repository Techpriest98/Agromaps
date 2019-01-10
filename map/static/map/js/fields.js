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
			console.log("map data length: ", mapData.length);
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