google.charts.setOnLoadCallback(drawRegionsMapWater);
google.charts.setOnLoadCallback(drawChart);
  function drawRegionsMapWater() {
    var data = google.visualization.arrayToDataTable([
      ["Country", "Customer Count", "Agent Count"],
      ["Argentina", 999000, 100],
      ["Australia", 969000, 450],
      ["Belgium", 12000, 200],
      ["Brazil", 850000, 250],
      ["Canada", 1110000, 590],
      ["China", 3975000, 690],
      ["Colombia", 4500, 100],
      ["Denmark", 78600, 150],
      ["France", 67000, 400],
      ["Germany", 140000, 550],
      ["India", 1060000, 560],
      ["Japan", 60000, 420],
      ["Nigeria", 1054000, 305],
      ["Philippines", 120000, 230],
      ["Russia", 2904000, 180],
      ["Singapore", 79000, 450],
      ["South Korea", 15000, 290],
      ["Switzerland", 35000, 230],
      ["United Kingdom", 4015000, 750],
    ]);

    var options = {
      colorAxis: {
        colors: [
          "#C6E2FF",
          "#0099CC",
          "#60AFFE",
          "#39B7CD",
          "#8EE5EE",
          "#00CDCD",
          "#8FD8D8",
          "#66CCCC",
          "#96CDCD",
        ],
      },
      legend: "none",
    };

    var chart = new google.visualization.GeoChart(
      document.getElementById("regions_div_water")
    );
    chart.draw(data, options);
  }
  $(document).ready(function () {
    $(window).resize(function () {
       
        drawRegionsMapWater();
     
      
    });
  });
