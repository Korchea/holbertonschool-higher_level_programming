toChange = document.querySelector("#toggle_header");
function doIt() {
    document.querySelector("header").classList.toggle("red");
    document.querySelector("header").classList.toggle("green");
}
toChange.addEventListener("click", doIt);
