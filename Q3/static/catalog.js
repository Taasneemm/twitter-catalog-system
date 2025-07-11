//during the loading of the page, table and title will be hidden
window.onload = function(){
    document.getElementById("catalog-html-table-title").style.display = 'none';
    document.getElementById("catalog-html-table-value").style.display = 'none';
    document.getElementById("catalog-tweet-count").style.display = 'none';

};

// add evenListener to submit button
document.querySelector("#submitButton").addEventListener("click", process);



function process(){
    var when = document.querySelector("#whenInput").value;
    var who = document.querySelector("#whoInput").value;
    var comment = document.querySelector("#commentInput").value;
    var about = document.querySelector("#aboutInput").value;
    var media = document.querySelector("#mediaInput").value;
    var what = document.querySelector("#whatInput").value;
    var whom = document.querySelector("#whomInput").value;
    var referenceId = document.querySelector("#referenceIdInput").value;

    alert(" " +when +" "+ " " +who +" "+ " " +comment +" "+ " " + about +" "+ " " +media +" "+ " " +what +" "+ " " +whom +" "+ " " +referenceId)

    // hide all the elements in the form
    // hide all the labels in the form
    document.getElementsByClassName("formLabel")[0].style.display = "none";
    document.getElementsByClassName("formLabel")[1].style.display = "none";
    document.getElementsByClassName("formLabel")[2].style.display = "none";
    document.getElementsByClassName("formLabel")[3].style.display = "none";
    document.getElementsByClassName("formLabel")[4].style.display = "none";
    document.getElementsByClassName("formLabel")[5].style.display = "none";
    document.getElementsByClassName("formLabel")[6].style.display = "none";
    document.getElementsByClassName("formLabel")[7].style.display = "none";

    // hide all the input fields in the form
    document.getElementById("whenInput").style.display = "none";
    document.getElementById("whoInput").style.display = "none";
    document.getElementById("commentInput").style.display = "none";
    document.getElementById("aboutInput").style.display = "none";
    document.getElementById("mediaInput").style.display = "none";
    document.getElementById("whatInput").style.display = "none";
    document.getElementById("whomInput").style.display = "none";
    document.getElementById("referenceIdInput").style.display = "none";
    document.getElementById("submitButton").style.display = "none";

    // get table id from html and insert rows 
    var table = document.getElementById("catalog-html-table-value");
    var row1 = table.insertRow(1);
    var row2 = table.insertRow(2);
    var row3 = table.insertRow(3);
    var row4 = table.insertRow(4);
    var row5 = table.insertRow(5);
    var row6 = table.insertRow(6);
    var row7 = table.insertRow(7);
    var row8 = table.insertRow(8);

    $.ajax({
        url:"/Q2bprocess",
        type: "POST",
        data:{when2b:when, who2b:who, comment2b:comment, about2b:about,
        media2b: media, what2b:what, whom2b: whom, referenceId2b: referenceId},
        error: function() {
            alert("Error");
        },
        success: function(data, status, xhr) {
            alert("success")
            // store the year
            var a = data.data
            // occurences of year
            var b = data.data1
            alert(a)
            document.querySelector("#catalog-tweet-count").innerHTML = "The Total Count of Tweets for year " +a +" is " +b;

            

        }
    
    })

    //insert values into row cells

    row1.insertCell(0).innerHTML = "When";
    row1.insertCell(1).innerHTML = when;
    row2.insertCell(0).innerHTML = "who";
    row2.insertCell(1).innerHTML = who;
    row3.insertCell(0).innerHTML = "Comment";
    row3.insertCell(1).innerHTML = comment;
    row4.insertCell(0).innerHTML = "About";
    row4.insertCell(1).innerHTML = about;
    row5.insertCell(0).innerHTML = "Media";
    row5.insertCell(1).innerHTML = media;
    row6.insertCell(0).innerHTML = "What";
    row6.insertCell(1).innerHTML = what;
    row7.insertCell(0).innerHTML = "Whom";
    row7.insertCell(1).innerHTML = whom;
    row8.insertCell(0).innerHTML = "Reference ID";
    row8.insertCell(1).innerHTML = referenceId;

    // show title and table
    document.getElementById("catalog-html-table-title").style.display = "inline";
    document.getElementById("catalog-html-table-value").style.display = "block";
    document.getElementById("catalog-tweet-count").style.display = 'block';


    
    

};




