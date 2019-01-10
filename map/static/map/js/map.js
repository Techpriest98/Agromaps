	var map;
	var infoWindow;

	var mapUrl = "map";
	var cultureUrl = "culture";
	var seedUrl = "seed";

	var fieldDetail = "";

	var wPath;

	document.getElementById('toggle-btn').onclick = function()
	{
		document.getElementById('sidebar-wrapper').classList.toggle('active');
		document.getElementById('toggle-btn').classList.toggle('active');
	}

	function initMap()
	{
		let seedRequest = new XMLHttpRequest();
		let mapRequest = new XMLHttpRequest();
		let cultureRequest = new XMLHttpRequest();

		let mapData;
		let cultureData;
		let seedData;

		seedRequest.open("GET", seedUrl);
		seedRequest.onload = function()
		{
			seedData = JSON.parse(seedRequest.responseText);
			cultureRequest.send();
		}
		cultureRequest.open("GET", cultureUrl);
		cultureRequest.onload = function()
		{
			cultureData = JSON.parse(cultureRequest.responseText);	
			mapRequest.send();
		}
		mapRequest.open("GET", mapUrl);
		mapRequest.onload = function()
		{
			mapData = JSON.parse(mapRequest.responseText);
			for(let i = 0; i < seedData.length; i++)
			{
				field ="";
				culture = "";
				for(let j = 0; j < mapData.length; j++)
				{
					console.log(seedData[i].field, mapData[j].pk)
					if(seedData[i].field == mapData[j].id)
						field = mapData[j]
				}
				for(let j = 0; j < cultureData.length; j++)
				{
					if(seedData[i].culture == cultureData[j].id)
						culture = cultureData[j]
				}
				DrawField(map, showArrays, culture, field, i);
			}
		}
		seedRequest.send();

		let options = {
			zoom:18,
			center:{lat:49.327839, lng:31.518580}
		}

		map = new google.maps.Map(document.getElementById('map'), options);
		infoWindow = new google.maps.InfoWindow;
	}

	function DrawField(map, fieldDetailFunc,  culture, field, id)
	{
		let fieldTriangle = new google.maps.Polygon({
		      	paths: JSON.parse(field.polygon),
		      	strokeColor: culture.color,
		      	strokeOpacity: 0.8,
		      	strokeWeight: 2,
		      	fillColor: culture.color,
		      	fillOpacity: 0.35
	    });
	    fieldTriangle.setMap(map);
	    fieldTriangle.addListener('click', function(event){
	    	showArrays(event, field, culture)
	    });
	}

	function showArrays(event, field, culture)
	{
	    // Replace the info window's content and position.
	    infoWindow.setContent("<h6>"+field.title+"<h6><p>"+culture.name+"</p><p>Площа: "+field.square+" км2</p>");
	    infoWindow.setPosition(event.latLng);

	    infoWindow.open(map);
	}