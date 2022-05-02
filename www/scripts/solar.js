updateChart();

let labels = [];

let solar = {
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
            myChart.data.datasets[0].data.push(row[2]);
            myChart.data.datasets[1].data.push(row[3]);

            //update array
            labels.push(row[1]);
            solar.voltage.push(row[2]);
            solar.current.push(row[3]);
            battery.voltage.push(row[4]);

            myChart.update();

            const average = (array) => array.reduce((a, b) => a + b) / array.length;

            //update left panels
            $('#bat-volt').html(battery.voltage[battery.voltage.length - 1]);
            $('#bat-avg').html(average(battery.voltage.map(Number)).toFixed(2));
            $('#s-v-avg').html(average(solar.voltage.map(Number)).toFixed(2));
            $('#s-c-avg').html(average(solar.current.map(Number)).toFixed(2));
        });
}