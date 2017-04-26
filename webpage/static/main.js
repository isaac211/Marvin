
$(document).ready(function() {
    console.log("Script Loaded");
});

function up() {
    msgOut("Up pressed!");
    console.log("Up");
}

function down() {
    msgOut("Down pressed!");
    console.log("Down");
}

function left() {
    msgOut("Left pressed!");
    console.log("Left");
}

function right() {
    msgOut("Right pressed!");
    console.log("Right");
}

function indTogg() {
    var light = document.getElementById("indLight");
    if (light.className === "circle-green") {
        light.className = "circle-red";
    }
    else {
        light.className = "circle-green";
    }
    msgOut("CO Updated");
    console.log("Toggled");
}

function msgOut(msg) {
    var msgBox = document.getElementById("msg");
    msgBox.innerHTML = msg;
}
