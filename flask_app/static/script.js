function search(e) {
  // e.preventDefault() is a method that stops the default nature of javascript.
  e.preventDefault();
  var searchForm = document.getElementById("searchForm");
  // create formData object from js and send it through a fetch post request.
  var form = new FormData(searchForm);
  // fetch collects data from the specific endpoint in superheroes.py
  fetch("http://127.0.0.1:5000/searching", { method: "POST", body: form })
    .then((res) => res.json())
    .then((data) => {
      // empty string
      let htmlString = "";
      // data is the json response from the api request
      for (const result of data.results) {
        // results is an array and result is each object in the array
        // htmlString + url
        htmlString = htmlString + `<img src=${result.image.url} /> <br>`;
      }
      //   response will be equal to the htmlString
      document.getElementById("response").innerHTML = htmlString;
    });
}
