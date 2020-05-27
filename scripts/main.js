// Liam Bessell, 5/27/20

function showDiv(x) {

    let div = null;

    if (x === 0) {
        div = document.getElementById("project_0");
    }
    else if (x === 1) {
        div = document.getElementById("project_1");
    }
    else if (x === 2) {
        div = document.getElementById("project_2");
    }
    else if (x === 3) {
        div = document.getElementById("project_3");
    }
    else {
        console.log("Error: Invalid projectDiv ID");
        return;
    }

    if (div.style.display === "none" || div.style.display === "") {
        div.style.display = "block";
    }
    else {
        div.style.display = "none";
    }

}