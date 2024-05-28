function fetchDataBar() {
  var chart = echarts.init(document.getElementById("bar"), "white", {
    renderer: "canvas",
  });
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/barChart",
    dataType: "json",
    success: function (result) {
      chart.setOption(result);
    },
  });

  var mydate = new Date();
  console.log("chartBar最近一次更新是在:" + mydate);
}




function fetchDataSA() {
  var chart = echarts.init(document.getElementById("stacked_area"), "white", {
    renderer: "canvas",
  });
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/stackedAreaChart",
    dataType: "json",
    success: function (result) {
      chart.setOption(result);
    },
  });

  var mydate = new Date();
  console.log("stackedAreaChart最近一次更新是在:" + mydate);
}

// $(
//     function () {
//         var chart = echarts.init(document.getElementById('timeline_pie'), 'white', {renderer: 'canvas'});
//         $.ajax({
//             type: "GET",
//             url: "http://127.0.0.1:5000/timeLineChart",
//             dataType: 'json',
//             success: function (result) {
//                 chart.setOption(result);
//             }
//         });
//     }
// );










//Dynamic lineChart

var old_data = [];

function fetchDataLine() {
  var chart = echarts.init(document.getElementById("line"), "white", {
    renderer: "canvas",
  });
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/lineChart",
    dataType: "json",
    success: function (result) {
      chart.setOption(result);
      old_data = chart.getOption().series[0].data;
    },
    error: function (res) {
      alert("error1");
    },
  });
}

function getDynamicData() {
  var chart = echarts.init(document.getElementById("line"), "white", {
    renderer: "canvas",
  });
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/lineChart/lineDynamicData",
    dataType: "json",
    success: function (result) {
      old_data.push([result.name, result.value]);
      chart.setOption({
        series: [{ data: old_data }],
      });
    },
    error: function (res) {
      alert("error1");
    },
  });
}

//pieChart
function fetchDataPie() {
  var chart = echarts.init(document.getElementById("pie"), "white", {
    renderer: "canvas",
  });
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/pieChart",
    dataType: "json",
    success: function (result) {
      chart.setOption(result);
    },
  });
  var mydate = new Date();
  console.log("pieChart最近一次更新是在:" + mydate);
}







//全局配置更新
//主动执行：每60000ms执行一次fetchData()
$(function () {

  fetchDataBar();
  setInterval(fetchDataBar, 60000);
  // fetchDataSA();
  // setInterval(fetchDataSA, 60000);

  fetchDataLine();
  setInterval(getDynamicData, 10000);

  fetchDataPie();
  setInterval(fetchDataPie,60000);
});
