## INTRODUCTION TO DATA SCIENCE COURSE PROJECT WEBSITE 

## A TEAM HAS NO NAME

### DATA VISUALIZATION CHARTS

#### Task 1
<html>
<head>

	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js"></script>
	<script type="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"></script>
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>

</head>


<body>

	<div class="container">
		<canvas id="BtypevsCrimes"></canvas>
	</div>

	<script>
		var btvcrime = document.getElementById('BtypevsCrimes').getContext('2d');
		$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/Task_1_result.csv',
			async: false,

			success: function(result){
				lines = result.split("\n") // split the values by the lines

				// convert the records to json values
				var records = lines.filter((s)=> s.length > 0).map((record) =>{
					details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
					details = details || []
					return {year:details[0],business_type:details[1],business_name:details[2],address:details[3],has_T:details[4],has_L:details[5],crime_type:details[6],crimes:details[7],arrests:details[8],OnPremises:details[9]}
				})

				headers = records[0]
				records.shift()

				var businesstype_crimenum = records.map((record) => {
					var obj = {x:record.business_type,z:record.crimes}
					return obj
				})

				result = records.reduce((r,a) => {
					r[a.business_type] = r[a.business_type] || [];
					r[a.business_type].push(parseInt(a.crimes));
					return r;
				}, {})
				

				function add(a, b) {
						return a + b;
				}

				result.a = result.a.reduce(add, 0);
				result.b = result.b.reduce(add, 0);
				result.c = result.c.reduce(add, 0);

				var data = [result.a, result.b, result.c]

				console.log(data)

				var scatterChart = new Chart(btvcrime, {
					type: 'bar',
					data: data,
					options: {
    scales: {
        xAxes: [{
            gridLines: {
                offsetGridLines: true
            }
        }]
    }
}
				});
			}
		})

	</script>

</body>
</html>

#### TASK 4
<html>
<head>

	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js"></script>
	<script type="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"></script>
	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>

</head>


<body>

	<div class="container">
		<canvas id="passedInspectionChart"></canvas>
		<canvas id="conditionalInspectionChart"></canvas>
		<canvas id="failedInspectionChart"></canvas>
	</div>

	<script>
		var passedInspectionChart = document.getElementById('passedInspectionChart').getContext('2d');
		var conditionalInspectionChart = document.getElementById('conditionalInspectionChart').getContext('2d');
		var failedInspectionChart = document.getElementById('failedInspectionChart').getContext('2d');
		$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/task4_result.csv',
			async: false,

			 success: function(result){
			 	//console.log(data.responseText

				lines = result.split("\n") // split the values by the lines

				// convert the records to json values
				var records = lines.filter((s)=> s.length > 0).map((record) =>{
				
				details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
				details = details || []
				return {name:details[0],address:details[1],avgRating:details[2],numPass:details[3],numCond:details[4],numFail:details[5]}
				
				})

				headers = records[0] // get the headers

				records.shift() // remove the first (headers) row

				var avgRatingValues = records.map((record) => record.avgRating)
				var passCounts = records.map((record) => record.numPass)
				var condCounts = records.map((record) => record.numCond)
				var failCounts = records.map((record) => record.numFail)

				var ratingToPass = records.map((record) => {
					var obj = {x:record.avgRating,y:record.numPass}
					return obj
				})

				var ratingToConditional = records.map((record) =>{
					var ob = {x:record.avgRating, y:record.numCond}
					return ob
				})

				var ratingToFail = records.map((record) => {
					var ob = {x:record.avgRating, y:record.numFail}
					return ob
				})

				// scatter plot for plotting average ratings vs number of passed inspections
				var scatterChart = new Chart(passedInspectionChart, {
			    type: 'scatter',
			    data: {
			        datasets: [{
			            label: 'Average Review Rating vs #Pass',
			            data: ratingToPass,
			            backgroundColor: 'Green'

			        }]
			    },
			    options: {
			        scales: {
			            xAxes: [{
			                type: 'linear',
			                position: 'bottom'
			            }]
			        }
			    }
				});

				// scatter plot for plotting average ratings vs number of conditional inspections
				var scatterChart = new Chart(conditionalInspectionChart, {
			    type: 'scatter',
			    data: {
			        datasets: [{
			            label: 'Average Review Rating vs #Conditional',
			            data: ratingToConditional,
			            backgroundColor: 'Orange'
			            
			        }]
			    },
			    options: {
			        scales: {
			            xAxes: [{
			                type: 'linear',
			                position: 'bottom'
			            }]
			        }
			    }
				});	

				// scatter plot for average ratings vs number of failed inspections
				var scatterChart = new Chart(failedInspectionChart, {
			    type: 'scatter',
			    data: {
			        datasets: [{
			            label: 'Average Review Rating vs #Fail',
			            data: ratingToFail,
			            backgroundColor: 'Red'

			        }]
			    },
			    options: {
			        scales: {
			            xAxes: [{
			                type: 'linear',
			                position: 'bottom'
			            }]
			        }
			    }
				});

			 }})

		
	</script>

</body>
</html>

#### Task 8
<html>
  <head>

    <title>Marker Clustering</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  
  </head>
  <body>

		<div id="map"></div>
		<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
		<script type="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"></script>

    <script>
			function getcsv(){
				$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/Task_8_result.csv',
					async: false,

					success: function(result){
						lines = result.split("\n") // split the values by the lines

						// convert the records to json values
						var records = lines.filter((s)=> s.length > 0).map((record) =>{
							details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
							details = details || []

							//business_name,address,inspection_date,years_alive,latitude,longitude

							return {business_name:details[0],address:details[1],inspection_date:details[2],years_alive:details[3],latitude:details[4],longitude:details[5]}
						})

						headers = records[0]
						records.shift()

						initMap(records)
					}
				})
			}

      function initMap(records) {

        var Gmap = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: {lat: 41.8781, lng: -87.6298}
        });

        // Add some markers to the map.
        // Note: The code uses the JavaScript Array.prototype.map() method to
        // create an array of markers based on a given "locations" array.
        // The map() method here has nothing to do with the Google Maps API.
				let markers = [];
				$.each(records, function(i, d){
					var marker = new google.maps.Marker({
						position: {lat: parseFloat(d.latitude), lng: parseFloat(d.longitude)},
						map: Gmap,
						title: d.business_name
					});

					let address = d.address;
					var infowindow = new google.maps.InfoWindow({
						content:  `<div class="container">
												<h3>${d.business_name}</h3>
												<p><b>Address:</b>${d.address}</p>
												<p><b>Failed Inspection on:</b>${d.inspection_date}</p>
												<p><b>Stayed in Business for:</b>${d.years_alive} years</p>
												</div>
												`
					});

					marker.addListener('click', function() {
      		infowindow.open(Gmap, marker);
					});

					markers.push(marker);
				});
        
        // Add a marker clusterer to manage the markers.
        var markerCluster = new MarkerClusterer(Gmap, markers,
					{imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m',
					maxZoom: 20
				});
			}
    </script>
    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC94Y9rHyYQQ9CCf4DbV8f9J0ER9nKIdUg&callback=getcsv">
    </script>

  </body>
</html>

### TEAM MEMBERS
- **Meghana Sanjay**
  < msanja3@uic.edu > 
  Meghana is a graduate student currently in her second semester at UIC. She's an energetic, enthusiastic, bubbly, jumpy, crazy sometimes lazy straight out of college girl and could dance before she learnt how to walk.
- **Joylyn Lewis**
  < jlewis39@uic.edu > 
  Joylyn is a graduate student in her first semester at UIC. She has over eight years of industry experience working as an SAP      consultant implementing ERP solutions. In her free time, she likes reading fiction, cooking and travelling.
- **Adarsh Hegde** < ahegde5@uic.edu >
  Adarsh is a graduate student in his second semester at UIC. He loves programming and football.
- **Stephen Walden** < swalde3@uic.edu >
  Stephen is an undergraduate student in his sixth semester at UIC. He started programming around computer games, and has started chasing a career in computer science. He has a year of experience working with Robotic Process Automation in the industry. He enjoys driving motorcycles and building with legos. [More about Stephen](https://walden1995.github.io/)

### WEEKLY STATUS REPORT
- The webpage for the Weekly Status Report is available [here](https://github.com/ateamhasnoname03/data_science/wiki/Weekly-Status-Report)
- The weekly status is also managed using the project board available [here](https://github.com/ateamhasnoname03/data_science/projects/1)

