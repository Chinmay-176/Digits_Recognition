var chart = "";
var firstTime = 0;
// var results=[9.222,345,121,544,662,1,2,2,66];
function loadChart(label, data, modelSelected) {
    var ctx = document.getElementById('chart_box').getContext('2d');
    chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
 
        // The data for our dataset
        data: {
            labels: label,
            datasets: [{
                label: modelSelected + " prediction",
                backgroundColor: '#f50057',
                borderColor: 'rgb(255, 99, 132)',
                data: data,
            }]
        },
 
        // Configuration options go here
        options: {}
    });
}
//----------------------------
// display chart with updated
// drawing from canvas
//----------------------------
function displayChart(data) {
    var select_option = "CNN";
 
    label = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    if (firstTime == 0) {
        loadChart(label, data, select_option);
        firstTime = 1;
    } else {
        chart.destroy();
        loadChart(label, data, select_option);
    }
    document.getElementById('chart_box').style.display = "block";
}
 
function displayLabel(data) {
    var max = data[0];
    var maxIndex = 0;
 
    for (var i = 1; i < data.length; i++) {
        if (data[i] > max) {
            maxIndex = i;
            max = data[i];
        }
    }
    $(".prediction-text").html("Predicting you draw <b>"+maxIndex+"</b> with <b>"+Math.trunc( max*100 )+"%</b> confidence")
}