import $ from "jquery";

const rootApp = document.getElementById("root");
rootApp.innerHTML = '<button id="toggleButton">ON</button>';

$("#toggleButton").click(function() {
    var button = $(this);
    if (button.text() === "ON") {
        button.text("OFF");
    } else {
        button.text("ON");
    }
});
