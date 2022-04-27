/*taken from https://www.youtube.com/watch?v=Y1JhMa22CoM*/

drawChart();
// setup 
async function drawChart() {
    const datapoints = await getData();

    const data = {
        labels: datapoints.labels,
        datasets: [{
            label: 'Solar Voltage',
            data: datapoints.solar.voltage,
            borderColor: [
                'rgba(255, 159, 28, 1)'
            ],
            tension: 0.15,
            yAxisID: 'y'
        },
        {
            label: 'Solar Current',
            data: datapoints.solar.current,
            borderColor: [
                'rgba(254, 215, 102, 1)'
            ],
            tension: 0.15,
            yAxisID: 'y1'
        }
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
        document.getElementById('solar-graph'),
        config
    );
}

async function getData() {
    //arrays to store data
    const labels = [];
    const solar = {
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
    console.log(tabledata)

    //parse csv
    //split by row
    const table = tabledata.split('\n').slice(1);

    //split by column
    table.forEach(row => {
        const column = row.split(',');
        labels.push(column[1]);

        solar.voltage.push(column[2]);
        solar.current.push(column[3]);

        battery.voltage.push(column[4]);
    });

    return {
        labels,
        solar,
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
        });
    });

    return filename;
}

window.onload = async function () {
    //update left panel values
    const data = await getData();
    const batData = data.battery.voltage;
    const solar = data.solar;

    const average = (array) => array.reduce((a, b) => a + b) / array.length;

    const battery = batData.map(Number);
    const volt = solar.voltage.map(Number);
    const cur = solar.current.map(Number);

    $('#bat-volt').html(batData[batData.length - 1]);
    $('#bat-avg').html(average(battery).toFixed(2));
    $('#s-v-avg').html(average(volt).toFixed(2));
    $('#s-c-avg').html(average(cur).toFixed(2));

    //set download link for session
    let filename = await getFilename();
    console.log(filename);
    document.getElementById('download-btn').setAttribute('href', "../" + filename);
}