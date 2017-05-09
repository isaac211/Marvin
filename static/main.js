
var commsocket;

$(document).ready(function() {
    console.log("Script Loaded");
    commsocket = io.connect("http://"+document.domain + ":" + location.port +
        "/commsocket");
    commsocket.on('connect', function() {
        console.log("Socket Connected");
    });
    commsocket.on('event', function(msg) {
        if (msg.type && msg.type == "CO") {
            if (msg.toggle) {
                indTogg();
            }
        }
    });
    window.setInterval(function() {
        commsocket.emit('event', {"type": "co_req"});
    }, 1000);
});

function up() {
    msgOut("Up pressed!");
    console.log("Up");
    var upMsg = {
        type: "move",
        direction: "forward"
    };
    commsocket.emit('event', upMsg);
}

function down() {
    msgOut("Down pressed!");
    console.log("Down");
    var downMsg = {
        type: "move",
        direction: "backward"
    };
    commsocket.emit('event', downMsg);
}

function left() {
    msgOut("Left pressed!");
    console.log("Left");
    var leftMsg = {
        type: "move",
        direction: "left"
    };
    commsocket.emit('event', leftMsg);
}

function right() {
    msgOut("Right pressed!");
    console.log("Right");
    var rightMsg = {
        type: "move",
        direction: "right"
    };
    commsocket.emit('event', rightMsg);
}

function stop() {
    msgOut("Stop pressed!");
    console.log("Stop");
    var stopMsg = {
        type: "move",
        direction: "stop"
    };
    commsocket.emit('event', stopMsg);
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
