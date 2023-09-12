async function doIt() {
    const names = await (await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")).json();
    document.querySelector("#character").innerHTML = names["name"];
}
doIt();
