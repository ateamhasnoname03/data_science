## INTRODUCTION TO DATA SCIENCE COURSE PROJECT WEBSITE 

## A TEAM HAS NO NAME

### DATA VISUALIZATION CHARTS
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"></script>
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>

### Crime/Business_Type Report:
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
			// remove header files
			headers = records[0]
			records.shift()
			// reduce functions for visualizing totals
			result = records.reduce((r,a) => {
				r[a.business_type] = r[a.business_type] || [];
				r[a.business_type].push(parseInt(a.crimes));
				return r;
			}, {})
			arrest_result = records.reduce((r,a) => {
				r[a.business_type] = r[a.business_type] || [];
				r[a.business_type].push(parseInt(a.arrests));
				return r;
			}, {})
			// redduction accumulation function
			function add(a, b) {
					return a + b;
			}
			//reduction
			result.a = result.a.reduce(add, 0);
			result.b = result.b.reduce(add, 0);
			result.c = result.c.reduce(add, 0);
			arrest_result.a = arrest_result.a.reduce(add, 0);
			arrest_result.b = arrest_result.b.reduce(add, 0);
			arrest_result.c = arrest_result.c.reduce(add, 0);
			//Cleaning variables and setting up chart.
			var crime_data = [result.a, result.b, result.c]
			var arrest_data = [arrest_result.a, arrest_result.b, arrest_result.c]
			var barChartData = {
				labels: ['Grocery Stores', 'Schools', 'Restaurants'],
				datasets: [{
					label: '#Crimes',
					backgroundColor: '#ff6384',
					borderColor: '#ff6384',
					borderWidth: 1,
					data: crime_data
				}, {
					label: '#Arrests',
					backgroundColor: '#36a2eb',
					borderColor: '#36a2eb',
					borderWidth: 1,
					data: arrest_data
				}]
			};
			var scatterChart = new Chart(btvcrime, {
			type: 'bar',
			data: barChartData,
			options: {
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: '#Crime and #Arrest Near Business Type'
				}
			}
		});
		}
	})
</script>

### Neighbourhood and Crime Data
<div class="container">
	<canvas id="NeighbourhoodvsCrimesProb"></canvas>
</div>

<script>
	var nvcrimep = document.getElementById('NeighbourhoodvsCrimesProb').getContext('2d');
	$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/output_task_2_trial1.csv',
		async: false,

		success: function(result){
			lines = result.split("\n") // split the values by the lines

			// convert the records to json values
			var records = lines.filter((s)=> s.length > 0).map((record) =>{
				details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
				details = details || []
				return {Address:details[0],Classifier:details[1],Prediction:details[2],Probability:details[3]}
            });headers = records[0]
			records.shift()

			var barChartData = {
				labels: ["001XX N MICHIGAN AVE","001XX N STATE ST","001XX W JACKSON BLVD","001XX W Jackson Blvd","001XX W MADISON ST","001XX W VAN BUREN ST","002XX N CLARK ST","002XX N LOWER MICHIGAN AVE","002XX N MICHIGAN AVE","003XX N LA SALLE ST"],
				datasets: [{
						label: 'DecisionTree',
						backgroundColor: 'Blue',
						borderColor: 'Blue',
						borderWidth: 1,
						data: [1,1,1,1,1,1,1,0.654676259,1,1]
				}, {
						label: 'LogisticRegression',
						backgroundColor: 'Yellow',
						borderColor: 'Yellow',
						borderWidth: 1,
						data: [0.552730493,0.553021972,0.552264041,0.520338855,0.548039461,0.549336873,0.55290906,0.544891359,0.552422311,0.527977161]
				}, {
						label: 'RandomForest',
						backgroundColor: 'Red',
						borderColor: 'Red',
						borderWidth: 1,
						data: [0.807631225,0.87074327,0.850573228,0.38595796,0.813417079,0.747034012,0.757487719,0.813385861,0.811604345,0.757636322]
				}]
			};

			var scatterChart = new Chart(nvcrimep, {
				type: 'bar',
				data: barChartData,
				options: {
					responsive: true,
					legend: {
						position: 'top',
					},
					title: {
							display: true,
							text: 'Crime Data by Neighbourhood'
					}
				}
			});            
		}
	});
</script>

### Age and Crime Data
<div class="container">
	<canvas id="agevsCrimes"></canvas>
</div>

<script>
	var nvcrime = document.getElementById('agevsCrimes').getContext('2d');
	$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/Output_task_3.csv',
		async: false,

		success: function(result){
			lines = result.split("\n") // split the values by the lines

			// convert the records to json values
			var records = lines.filter((s)=> s.length > 0).map((record) =>{
				details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
				details = details || []
				return {address:details[0],Population:details[1],above18:details[2],below18andover64:details[3]}
            });
			headers = records[0]
			records.shift()

			var barChartData = {
				labels: ["Loop","Near West Side","Near South Side"],
				datasets: [{
						label: 'Above 18',
						backgroundColor: 'Blue',
						borderColor: 'Blue',
						borderWidth: 1,
						data: [1669,1048,5872]
				}, {
						label: 'Below 18 and over 64',
						backgroundColor: 'Yellow',
						borderColor: 'Yellow',
						borderWidth: 1,
						data: [3953,4663,12183]
				}, {
						label: 'Population',
						backgroundColor: 'Red',
						borderColor: 'Red',
						borderWidth: 1,
						data: [29283,21390,54881]
				}]
			};

			var scatterChart = new Chart(nvcrime, {
				type: 'bar',
				data: barChartData,
				options: {
					responsive: true,
					legend: {
						position: 'top',
					},
					title: {
						display: true,
						text: 'Crime Data by Age Demographic'
					}
				}
			});
		}
	});
</script>

### Review Ratings Vs. Food Inspection Results
<script>
	$('document').ready(function(){
		document.getElementById('chartType').addEventListener('change', function(e) {
			populate_graph()
		});
	});
</script>

<div class="container">
	<canvas id="InspectionChart"></canvas>
	<select id="chartType">
			<option value="pass">Passed Inspections</option>
			<option value="conditional">Conditional Inspections</option>
			<option value="fail">Fail Inspections</option>
	</select>
</div>

<script>
	var InspectionChart = document.getElementById('InspectionChart').getContext('2d');
	
	populate_graph()
	function populate_graph(){
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

			// get and remove headers row
			headers = records[0]
			records.shift()

			//perform maps for obtaining ploting data
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

			var elem = document.getElementById("chartType");
				var value = elem.options[elem.selectedIndex].value;
				var text = elem.options[elem.selectedIndex].text;
				var graph_data = ''
				if (value == 'pass'){
					graph_data = ratingToPass
					graph_label = '#Pass'
					graph_color = 'Green'
				} else if (value == 'conditional'){
					graph_data = ratingToConditional
					graph_label = '#Conditional'
					graph_color = 'Orange'
				} else if (value == 'fail'){
					graph_data = ratingToFail
					graph_label = '#Fail'
					graph_color = 'Red'
				}
			console.log(graph_data)

			// scatter plot for plotting average ratings vs number of passed inspections
			var scatterChart = new Chart(InspectionChart, {
				type: 'scatter',
				data: {
						datasets: [{
								label: 'Average Review Rating vs '+graph_label,
								data: graph_data,
								backgroundColor: graph_color

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
	}	
</script>

### Sentiment Analysis
<div class="container">
	<canvas id="pos_neg_rating"></canvas>
</div>

<script>
	var pos_neg_rating = document.getElementById('pos_neg_rating').getContext('2d');
	$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/SentimentAnalysis.csv',
		async: false,

		success: function(result){
			// split the values by the lines
			lines = result.split("\n")
			// convert the records to json values
			var records = lines.filter((s)=> s.length > 0).map((record) =>{
				details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
				details = details || []
				return {name:details[1],reviewContent:details[2],rating:details[3],sentimentLabel:details[4]}
			})

			// remove the first (headers) row
			records.shift()

			//get restarant_names
			var restaurant_names = new Set(records.map((record) => record.name))
			//verify last line
			console.log(restaurant_names)
			
			// group the records by the the restaurant name
			mod_records = records.reduce((r, a)=> {
					r[a.name] = r[a.name] || [];
					r[a.name].push(a);
					return r;
				},{});
			//result = []
			//verify last line
			console.log(mod_records)

			output = new Array()
			restaurant_names.forEach( function(item) {
				details_list = mod_records[item]
				count = details_list.length
				restaurant = details_list[0].name
				total_rating = 0
				count_pos = 0
				count_neg = 0
				details_list.forEach( function(detail) {
					//console.log(detail)
					if(detail.sentimentLabel == "Positive") count_pos++;
					else if(detail.sentimentLabel == "Negative") count_neg++;
					total_rating = total_rating + parseInt(detail.rating)
				})
				output.push({name:restaurant, positive:count_pos, negative:count_neg, rating:Math.round((total_rating/count)*100)/100})
			})
			
			positive_labels = output.map((rec) => {
				var ob = {x:rec.rating, y:rec.positive}
				return ob
			})
			negative_labels = output.map((rec) => {
				var ob = {x:rec.rating, y:rec.negative}
				return ob
			})
			rating_points = output.map((rec) => rec.rating)

			var label_rating_chart = new Chart(pos_neg_rating,{
				type: 'scatter',
				data: {
					datasets: [{
						label: 'Positive Label',
						data: positive_labels,
						backgroundColor: 'Green'
					},
					{
						label: 'Negative Label',
						data: negative_labels,
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
			})
		}
	})
</script>
	
### Task 7
#### Yelp Restaurant Review Rating Chart
<div class="container">
	<canvas id="reviewRatingChart" width="50" height="25"></canvas>
</div>
<script>
	var reviewRatingChart = document.getElementById('reviewRatingChart').getContext('2d');
	$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/task7_output.csv',
		async: false,
		success: function(result){
		 	//console.log(data.responseText
			lines = result.split("\n") // split the values by the lines
			// convert the records to json values
			var records = lines.filter((s)=> s.length > 0).map((record) =>{
				details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
				details = details || []
				return {review:details[0],reviewRating:details[1]}
			})
			//get and remove headers
			headers = records[0]
			records.shift()
			//map data
			var reviewRatingValues = records.map((record) => record.reviewRating)
			count_1=count_2=count_3=count_4=count_5 = 0 
			reviewRatingValues.forEach(function(item) {
				//console.log(item)
				if(item == "1") count_1++;
				else if(item == "2") count_2++;
				else if(item == "3") count_3++;
				else if(item == "4") count_4++;
				else if(item == "5") count_5++;
			})
			// pieChart for plotting review ratings
			var pieChart = new Chart(reviewRatingChart,{
		    type: 'pie',
		    data: {
					labels: ["Review Rating 1", "Review Rating 2", "Review Rating 3", "Review Rating 4", "Review Rating 5"],
					datasets: [{
						data: [count_1,count_2,count_3,count_4,count_5],
						//data: [1000,2000,3000,4000,5000],
						backgroundColor: [
							"red", 
							"orange", 
							"yellow", 
							"blue",
							"green"
						]
					}]
		    }
			});	
		}
	})
</script>

### Task 8
#### Food inspection viability and interactive map.
{% include google-map.html latitude=41.8781 longitude=-87.6298 zoom=15 %}



### Task 10
#### Predicting probabilities of each type of robbery against census blocks for Summer 2018 

<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js"></script>
<script type="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"></script>
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$(document).ready(function()
{
    $("button").click(function()
	{
		// all code should go here
		var selMonth = document.getElementById('selectedMonth').value;
		var robberyByCensusChart = document.getElementById('robberyByCensusChart').getContext('2d');
		$.ajax({url :'https://cors.io/?https://raw.githubusercontent.com/ateamhasnoname03/data_science/master/Data%20Integration%20and%20Analytics/output/task10_output.csv',
		async: false,

		 success: function(result){
		 	//console.log(data.responseText

			lines = result.split("\n") // split the values by the lines

			// convert the records to json values
			var records = lines.filter((s)=> s.length > 0).map((record) =>{
			
			details = record.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g)
			details = details || []
			return {censusBlock:details[0],month:details[1],avgTemp:details[2],robberyType:details[3],probability:details[4]}
			
			})

			headers = records[0] // get the headers

			records.shift() // remove the first (headers) row

			var censusBlockValues = records.map((record) => record.censusBlock)
			var monthValues = records.map((record) => record.month)
			var avgTempValues = records.map((record) => record.avgTemp)
			var robberyTypeValues = records.map((record) => record.robberyType)
			var probabilityValues = records.map((record) => record.probability)
			
			var probabilityToCensusBlock_Aggravated = records.map((record) => {
				if (record.robberyType.trim() === 'AGGRAVATED' && record.month == selMonth) {
						var obj1 = {x:record.censusBlock,y:record.probability}
					}selMonth
					return obj1
			})
			
			var probabilityToCensusBlock_Armed = records.map((record) => {
				if (record.robberyType.trim() === 'ARMED' && record.month == selMonth) {
					var obj2 = {x:record.censusBlock,y:record.probability} }
				return obj2
			})
			
			var probabilityToCensusBlock_Attempt = records.map((record) => {
				if (record.robberyType.trim() === 'ATTEMPT' && record.month == selMonth) {
					var obj3 = {x:record.censusBlock,y:record.probability} }
				return obj3
			})
			
			var probabilityToCensusBlock_Strongarm = records.map((record) => {
				if (record.robberyType.trim() === 'STRONGARM - NO WEAPON' && record.month == selMonth) {
					var obj4 = {x:record.censusBlock,y:record.probability} }
				return obj4
			})
			
			var probabilityToCensusBlock_Vehicular = records.map((record) => {
				if (record.robberyType.trim() === 'VEHICULAR HIJACKING' && record.month == selMonth) {
					var obj5 = {x:record.censusBlock,y:record.probability} }
				return obj5
			})
			

			// scatter plot for plotting probabilities vs census blocks
			var scatterChart = new Chart(robberyByCensusChart, {
		    type: 'line',
		    data: {
			
			labels: ['2801001025', '2819001001', '3201001008', '3201001017', '3201001020', '3201002021', '3201002023', '3201002026', '3201002030', '3201002034', '3201003009', '3204001020', '3204001035', '3204001036', '3204001043', '3206001010', '3206002005', 
					'3301001000', '3301001001', '3301001007', '3301003009', '8391001020', '8391001023', '8391001033', '8391001034', '8391001037', '8391001038', '8391001045', '8391001049', '8391001056', '8391001057', '8391001062', '8391001064', '8391001068', 
					'8391001093', '8391001096', '8391001102', '8391001107', '8391002000', '8391002008', '8391002013', '8391002021', '8391002046'],
			 datasets: [
			 {
		        label: 'Aggravated',
		        data: probabilityToCensusBlock_Aggravated,
		        backgroundColor: 'Yellow',
				showLine: true

		    },
			{
		        label: 'Armed',
		        data: probabilityToCensusBlock_Armed,
		        backgroundColor: 'Red',
				showLine: true

		    },
			{
		        label: 'Attempt',
		        data: probabilityToCensusBlock_Attempt,
		        backgroundColor: 'Orange',
				showLine: true

		    },
			{
		        label: 'Strongarm - No Weapon',
		        data: probabilityToCensusBlock_Strongarm,
		        backgroundColor: 'Green',
				showLine: true

		    },
			{
		        label: 'Vehicular Hijacking',
		        data: probabilityToCensusBlock_Vehicular,
		        backgroundColor: 'Purple',
				showLine: true

		    }]
		    },
		    options: {
				scales: {
					xAxes: [{
						ticks: {
							autoSkip : false
								},					
		               type: 'category'
		            },		
					]
		        }
				}
			//new chart closes
		    });
			}
			//result closes here
			})
			//.ajax closes here
		 })
		 //click closes here
});
</script>
</head> 
<body>
<div class="container">
	<label id="selectMonth"><b>Select the month</b></label>
	<select id ="selectedMonth">
		<option value = "6">June 2018</option>
		<option value = "7">July 2018</option>
		<option value = "8">August 2018</option>
		<option value = "9">September 2018</option>
	</select>
	<button id="selMonthBtn">Get Monthly Data</button>
	<canvas id="robberyByCensusChart"></canvas>
</div>
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

