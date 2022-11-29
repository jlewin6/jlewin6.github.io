var socket;

function createMap(data, elementDiv, socketio)
{
	socket = socketio
	// enter code to define margin and dimensions for svg
	var margin = {top: 95, right: 0, bottom: 80, left: 150};
	var width = 1100 - margin.left - margin.right,
	height = 500 - margin.top - margin.bottom;

	// enter code to create svg
	let svg = d3.select(elementDiv)
				.append("svg")
				.attr("id", "choropleth")
				.attr("width", width + margin.left + margin.right)
				.attr("height", height + margin.top + margin.bottom);
	
	// enter code to create color scale
	colours = d3.scaleQuantile()
					.range(d3.schemeOranges[4]);
	
	// enter code to define tooltip
	
	// enter code to define projection and path required for Choropleth
	// For grading, set the name of functions for projection and path as "projection" and "path"
	var projection = d3.geoNaturalEarth();
	var path = d3.geoPath().projection(projection);

	// define any other global variables
	let pathToJson = 'static/custom.geo.json';
	Promise.resolve(d3.json(pathToJson)).then((values) => {
		world = values;
		createMapAndLegend(world, data, path);
	});
    
}

function createMapAndLegend(world, data, path)
{	
	let countsArray = [];
	for(d in data) {
		countsArray.push(data[d].counts);
		//console.log(data[d].name + " : " + data[d].counts);
	}
	colours.domain(countsArray.sort(d3.ascending));

	let t = d3.select("#tooltip");
    t.remove();

	let tip = d3.tip()
				.attr("id", "tooltip")
				.style("background", "black")
				.html(function(d) {
						if(d != null) {
							return  "<text style='color: white'>" +
								"Country:" + d.name + "<br>" +
								"Trial Count:" + d.counts + "<br>" +
								"</text>";
						} else {
							return  "<text style='color: white'>" +
								"No data available" + "<br>" +
								"</text>";
						}                      
	});	

	let svg = d3.select("svg");
	
	svg.call(tip);

	svg.selectAll('*').remove();

	svg.append("g")
	   .attr("id", "countries")
	   .selectAll("path")
	   .data(world.features)
	   .enter()
	   .append("path")
	   .attr("d", path)
	   .attr("fill", function (d) {
			let countryName = d.properties.name;
			let found = false;
			let studyData = {};
			for(c in data) {
				if(data[c].name === countryName){
					found = true;
					studyData = data[c];
					break;
				}
			}
			if(found){
				return colours(studyData.counts);
			} else{
				return "gray";
			}
        })
		.on("mouseover", function (d) {
                    let countryName = d.properties.name;
					let studyData = null;
                    for(c in data) {
						if(data[c].name === countryName){
							found = true;
							studyData = data[c];
							break;
						}
					}

                    return tip.show(studyData)
            })
        .on("mouseout",  tip.hide)
		.on("click", function (d) {
			displayCountryDetailsData(d);
		});
		
	let legend = d3.legendColor()
					.labelFormat(d3.format(".0f"))
					.scale(colours);

	svg = d3.select("svg");
	svg.append("g")
	   .attr("id", "legend");
	d3.select("#legend")
	  .attr("transform", "translate(960,10)")
	  .call(legend);
}

function displayCountryDetailsData(country)
{
	document.getElementById('countryName').innerHTML =  '';
	document.getElementById("genderData").innerHTML = '';
	document.getElementById("studyTypeData").innerHTML = '';
	socket.emit("get_country_details_data", {'name' : country.properties.name});
	
	socket.on("get_country_details_data_done", (data) => {
		
		document.getElementById('countryName').innerHTML = "Country : " + country.properties.name;
		
		table = document.getElementById("genderData");
		table.innerHTML = '';
		table.innerHTML = '<tr><th>Gender</th><th>Count</th></tr>';
		
		let genderData = data['genderData'];
		let tr;
		let td;
		
		if(genderData['All']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = genderData['All']['name'];
			td = tr.insertCell();
			td.innerHTML = genderData['All']['counts'];
		}
		
		if(genderData['Male']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = genderData['Male']['name'];
			td = tr.insertCell();
			td.innerHTML = genderData['Male']['counts'];
		}
		
		if(genderData['Female']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = genderData['Female']['name'];
			td = tr.insertCell();
			td.innerHTML = genderData['Female']['counts'];
		}
		
		if(genderData['null']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = 'None';
			td = tr.insertCell();
			td.innerHTML = genderData['null']['counts'];
		}

		
		table = document.getElementById("studyTypeData");
		table.innerHTML = '';
		table.innerHTML = '<tr><th>Study Type</th><th>Count</th></tr>';
		
		let studyTypeData = data['studyTypeData'];
		
		if(studyTypeData['Interventional']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Interventional']['name'];
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Interventional']['counts'];
		}
				
		if(studyTypeData['Observational']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Observational']['name'];
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Observational']['counts'];
		}
		
		if(studyTypeData['Observational [Patient Registry]']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Observational [Patient Registry]']['name'];
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Observational [Patient Registry]']['counts'];
		}
		
		if(studyTypeData['Expanded Access']){
			tr = table.insertRow();
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Expanded Access']['name'];
			td = tr.insertCell();
			td.innerHTML = studyTypeData['Expanded Access']['counts'];
		}
		
	});
}