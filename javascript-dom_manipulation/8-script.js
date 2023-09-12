async function doIt() {
    const hello = await (await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")).json();
    document.querySelector("#hello").innerHTML += hello["hello"];
}
doIt();
