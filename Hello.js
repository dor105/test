var start = new Date().getTime();

document.getElementById("shape").onclick = function () {

    document.getElementById("shape").style.display = "none";
    var end = new Date().getTime();
    var timeTake = (end - start) / 100;
    document.getElementById("timetake").innerHTML = timeTake + "Sec";
    
}
