/*
 * Author: Sakthi Santhosh
 * Created on: 23/04/2023
 */
let counter = 1;
let socketHandle = io();

socketHandle.on("new_data", data => {
    let imageElement = document.getElementById("image-data");
    let imageDescriptionElement = document.getElementById("image-description");
    let newRow = document.createElement("tr");
    let rowContent = [];
    let prediction = parseFloat(data.prediction);
    let progressbarElement = document.getElementById("progressbar");
    let tableBodyElement = document.getElementById("table-body");
    let viewInMapElement = document.createElement("a");

    viewInMapElement.className = "btn btn-primary";
    viewInMapElement.href = "http://www.google.com/maps/place/" + data.location;
    viewInMapElement.textContent = "View in Map";

    for (let i = 0; i < 5; i++)
        rowContent[i] = document.createElement("td");

    rowContent[0].textContent = counter++;
    rowContent[1].textContent = data.datetime;
    rowContent[2].textContent = data.name;
    rowContent[3].textContent = data.prediction;
    rowContent[4].appendChild(viewInMapElement);

    for (let i = 0; i < 5; i++)
        newRow.appendChild(rowContent[i]);

    progressbarElement.style.width = prediction * 100 + '%';
    progressbarElement.innerHTML = prediction * 100 + '%';

    if (prediction > 0.75) {
        rowContent[3].className = "text-danger";

        let notifierElement = document.getElementById("notifier");

        notifierElement.style.display = "block";
        setTimeout(function() {
            notifierElement.style.display = "none";
        }, 5000);
    }

    tableBodyElement.appendChild(newRow);
    imageElement.src = "data:image/png;base64," + data.image;
    imageDescriptionElement.textContent = data.datetime;
})
