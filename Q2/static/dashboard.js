var ctx = document.getElementById("q2c_myChart").getContext('2d');
var ytx = document.getElementById("ECA_myChart").getContext('2d');
console.log("Imran Boss")




var r = document.getElementById("ECAbi").onclick = function() {

  document.getElementById('q2c_myChart').style.display = 'none';
  
  
  //alert("Hello Tasneem")
  r = document.getElementById("year2bi").value
  //alert(r)

  $.ajax({
    url: "ECA2ciiProcess",
    type: "POST",
    data: r,
    error: function() {
      alert("Error")
    },

    success: function(data, status, xhr) {
      //alert("came back from ECA2ciiProcess")

      var month = data.monthList
      var count = data.counts

      // alert(month)
      // alert(count)

      var averages = data.averages;
      var vLabels = [];
      var vData = [];

      for (const [key, values] of Object.entries(count)) {
      vLabels.push(key);
      vData.push(values);
      } 

      // alert(vLabels)
      // alert(vData)

      // let chartStatus = Chart.getChart(myChart);
      // if (chartStatus != undefined) {
      //   chartStatus.destroy();
      // }

      // myChart.destoy();

      if(window.myChart != null){
        window.myChart.destroy();
      }

      
      // line 55 put var myChart
      window.myChart = new Chart(ytx, {
      data: {
      labels: vLabels,
      datasets: []
      },
      options: {
          responsive: false
      }
      });

      debugger
      myChart.data.datasets.push({
      label: "# of Twitter Messages Per Month",
      type: "bar",
      // borderColor: '#'+(0x1ff0000+Math.random()*0xffffff).toString(16).substr(1,6),
      borderColor: '#'+(0x1100000+Math.random()*0xffffff).toString(16).substr(1,6),
      backgroundColor: "rgba(176, 142, 13, 1)",
      //backgroundColor: "rgba(249, 238, 236, 0.74)",
      data: vData,
      spanGaps: true
      });
      
      myChart.update();
    }

  })

}
console.log(r)



// $.ajax({
//   url:"Dashboard",
//   type:"POST",
//   data: [],
//   error: function() {
//     alert("Error")
//   },

//   success: function(data, status, xhr) {
//     alert("success Boss")


//   }
// })

$.ajax({
  url:"q2c_graphData",
  type:"POST",
  data: {},
  error: function() {
      alert("Error");
  },

  success: function(data, status, xhr) {

    debugger

    var years = data.year
    // alert(years)

    var select = document.createElement("select");
    select.name = "year2bi";
    select.id = "year2bi"

    for (const val of years) {
      var option = document.createElement("option");
      option.value = val;
      option.text = val.charAt(0).toUpperCase() + val.slice(1);
      select.appendChild(option);
    }

    var label = document.createElement("label");
    label.innerHTML = "Select Period: "
    label.htmlFor = "year2bi";
    

    document.getElementById("ECAbi").appendChild(label).appendChild(select);

    console.log("troll")
    

    var averages = data.averages;
    var vLabels = [];
    var vData = [];

    for (const [key, values] of Object.entries(averages)) {
      vLabels.push(key);
      vData.push(values);
    } 

    var myChart = new Chart(ctx, {
      data: {
      labels: vLabels,
      datasets: []
      },
      options: {
          responsive: false
      }
    });

    debugger
    myChart.data.datasets.push({
    label: "# of Twitter Messages Per Year",
    type: "bar",
    // borderColor: '#'+(0x1ff0000+Math.random()*0xffffff).toString(16).substr(1,6),
    borderColor: '#'+(0x1100000+Math.random()*0xffffff).toString(16).substr(1,6),
    backgroundColor: "rgba(176, 142, 13, 1)",
    //backgroundColor: "rgba(249, 238, 236, 0.74)",
    data: vData,
    spanGaps: true
    });
    myChart.update();
    }

})



  


    
      
      
  
    
  