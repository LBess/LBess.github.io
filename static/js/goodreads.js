//let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
//let DOMParser = require("xmldom").DOMParser;

const currentlyReadingURL = "https://www.goodreads.com/review/list/94131787-liam-b?shelf=currently-reading";

console.log("Getting...");
let request = new XMLHttpRequest();
request.open("GET", currentlyReadingURL);
request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
        //console.log(request.responseText);
        //let div = window.content.document.createElement('div');
        //div.innerHTML = request.responseText;
        let parser = new DOMParser();
        let dom = parser.parseFromString(request.responseText, "text/xml");

        bookTable = dom.getElementById("books");

        document.getElementById("recently-read-books").innerHTML = bookTable;
        console.log("Set");
    }
};

request.send(null);