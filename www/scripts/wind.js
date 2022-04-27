/*taken from https://www.youtube.com/watch?v=Y1JhMa22CoM*/

drawChart();
// setup 
async function drawChart() {
	const datapoints = await getData();

	const data = {
		labels: datapoints.labels,
		datasets: [{
			label: 'Wind Voltage',
			data: datapoints.wind.voltage,
			borderColor: [
				'rgba(68, 118, 4, 1)',
			],
			tension: 0.15,
			yAxisID: 'y'
		},
		{
			label: 'Wind Current',
			data: datapoints.wind.current,
			borderColor: [
				'rgba(108, 197, 81, 1)',
			],
			tension: 0.15,
			yAxisID: 'y1'
		},
		]
	};

	Chart.defaults.font.family = "Verdana";

	// config 
	const config = {
		type: 'line',
		data,
		options: {
			scales: {
				y: {
					beginAtZero: true,
					display: true,
					position: 'left',

					title: {
						display: true,
						text: 'voltage'
					}
				},
				y1: {
					beginAtZero: true,
					display: true,
					position: 'right',

					grid: {
						drawOnChartArea: false
					},

					title: {
						display: true,
						text: 'current'
					}
				}
			}
		}
	};

	// render init block
	const myChart = new Chart(
		document.getElementById('wind-graph'),
		config
	);
}

async function getData() {
	//arrays to store data
	const labels = [];
	const wind = {
		voltage: [],
		current: []
	};
	const battery = {
		voltage: []
	};

	//fetch csv
    const url = '/data';
    const response = await fetch(url, {
        'content-type': 'text/csv;charset=UTF-8'
    });
    const tabledata = await response.text();

	//parse csv
	//split by row
	const table = tabledata.split('\n').slice(1);

	//split by column
	table.forEach(row => {
		const column = row.split(',');
		labels.push(column[1]);

		wind.voltage.push(column[5]);
		wind.current.push(column[6]);

		battery.voltage.push(column[7]);
	});

	return {
		labels,
		wind,
		battery
	};
}

// gets filename from txt file so fetch can read the csv
// to whoever has to modify this in the future, sorry it's scuffed
async function getFilename() {
	let filename = $.get('../filename.txt', function (file) {
		const lines = file.split("\r\n");
        //this file should only ever have one line
		lines.forEach(row => {
			filename = String(row);
			console.log(filename);
		});
	});
	return filename;
}

window.onload = async function () {
	//update battery voltage
	const data = await getData();
	const batData = data.battery.voltage;
	$('#bat-volt').html(batData[batData.length - 1]);

	//set download link for session
	let filename = await getFilename();
	document.getElementById('download-btn').setAttribute('href',"../" + filename);
}