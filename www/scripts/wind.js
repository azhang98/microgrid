updateChart();

let labels = [];

let wind = {
    voltage: [],
    current: []
};

let battery = {
    voltage: []
};

//push new values every 1.5 seconds
function updateChart() {
    setInterval(getData, 1500);
}

async function getData() {
    //fetch csv from url
    const url = '/data';
    fetch(url, {
            'content-type': 'text/csv;charset=UTF-8'
        })
        .then(data => data.text(), error => console.warn("Failed to fetch data"))
        .then(tabledata => {
            //split by row
            const table = tabledata.split('\n').slice(1);

            //get last row
            const row = table[table.length - 1].split(',');

            //display 30 data points on the graph at anytime
            if (myChart.data.labels.length > 30) {
                myChart.data.labels.shift();
                myChart.data.datasets[0].data.shift();
                myChart.data.datasets[1].data.shift();
            }
            //update chart
            myChart.data.labels.push(row[1]);
            myChart.data.datasets[0].data.push(row[5]);
            myChart.data.datasets[1].data.push(row[6]);

            //update array
            labels.push(row[1]);
            wind.voltage.push(row[5]);
            wind.current.push(row[6]);

            myChart.update();

            const average = (array) => array.reduce((a, b) => a + b) / array.length;

            //update left panels
            $('#bat-volt').html(average(wind.voltage.map(Number)).toFixed(2));
            $('#bat-cur').html(average(wind.current.map(Number)).toFixed(2));
        });
}