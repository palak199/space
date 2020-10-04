
  google.charts.load("current", { packages: ["geochart", "corechart"] });
  google.charts.setOnLoadCallback(drawRegionsMapWaste);
  google.charts.setOnLoadCallback(drawChart);

  function drawRegionsMapWaste() {
    var data = google.visualization.arrayToDataTable([
      
 ["country_name" , "organic waste %" ],
 ["Aruba" , 0] ,
 ["Afghanistan" , 0] ,
 ["Angola" , 51.8 ],
 ["Albania" , 51.4 ],
 ["Andorra" , 31.2 ],
 ["United Arab Emirates " , 39 ],
 ["Argentina" , 38.74 ],
 ["Armenia" , 57 ],
 ["American Samoa" , 19.7 ],
 ["Antigua and Barbuda" , 46 ],
 ["Australia" , 48.44 ],
 ["Austria" , 31.4 ],
 ["Azerbaijan" , 45.19 ],
 ["Burundi" , 81 ],
 ["Belgium" , 14.18 ],
 ["Benin" , 52.1 ],
 ["Burkina Faso" , 21 ],
 ["Bangladesh" , 80.58 ],
 ["Bulgaria" , 24.35 ],
 ["Bahrain" , 59.1 ],
 ["Bahamas" , 46 ],
 ["Bosnia and Herzegovina" , 0],
 ["Belarus" , 30 ],
 ["Belize" , 47 ],
 ["Bermuda" , 17 ],
 ["Bolivia" , 55.1969111969112 ],
 ["Brazil" , 51.4 ],
 ["Barbados" , 18.3 ],
 ["Brunei Darussalam" , 36 ],
 ["Bhutan" , 58 ],
 ["Botswana" , 8.1 ],
 ["Central African Republic" , 0],
 ["Canada" , 24 ],
 ["Switzerland" , 29 ],
 ["Channel Islands" , 0],
 ["China" , 61.2 ],
 ["Dominica " , 45 ],
 ["Denmark " , 12.78 ],
 ["Dominican Republic " , 51 ],
 ["Algeria " , 54.4 ],
 ["Ecuador " , 58.67 ],
 ["Egypt, Arab Rep. " , 56 ],
 ["Eritrea " , 0],
 ["Spain " , 49 ],
 ["Estonia " , 36.7 ],
 ["Ethiopia " , 87.6 ],
 ["Finland " , 35.88 ],
 ["Fiji " , 33.2 ],
 ["France " , 32 ],
 ["Faeroe Islands " , 0],
 ["Micronesia, Fed. Sts." , 23.83 ],
 ["Gabon" , 0],
 ["United Kingdom" , 16.7 ],
 ["Equatorial Guinea" , 0],
 ["Greece" , 40 ],
 ["Grenada" , 27.1 ],
 ["Greenland" , 42.8 ],
 ["Guatemala" , 37.7144911834619 ],
 ["Guam" , 27.3 ],
 ["Guyana" , 50.1 ],
 ["India" , 0],
 ["Ireland" , 16.6 ],
 ["Iran" , 72.9 ],
 ["Iraq" , 68.7 ],
 ["Iceland" , 10 ],
 ["Israel" , 34 ],
 ["Italy" , 34.4 ],
 ["Jamaica" , 62.22 ],
 ["Jordan" , 50 ],
 ["Japan" , 36 ],

    ]);

    var options = {
      colorAxis: {
        colors: [
          "#228B22",
          "#008000",
          "#006400",
          "#ADFF2F",
          "#00FF00",
          "#32CD32",
          "#6B8E23",
          "#556B2F",
          "#663096",
          "#556B2F",
        ],
      },
      legend: "none",
    };

    var chart = new google.visualization.GeoChart(
      document.getElementById("regions_div_waste")
    );
    chart.draw(data, options);
  }

  $(document).ready(function () {
    $(window).resize(function () {
      drawRegionsMapWaste();
    });
  });


