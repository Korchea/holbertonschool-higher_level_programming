async function doIt() {
    const titles = await (await fetch("https://swapi-api.hbtn.io/api/films/?format=json")).json();
    const titleList = titles["results"]
    for (titleIndex in titleList) {
        document.querySelector("#list_movies").innerHTML += '<li>' + titleList[titleIndex]["title"] + '</li>';
    }
}
doIt();
