toChange = document.querySelector("#red_header");
function doIt() {
    document.querySelector("header").classList.add("red");
}
toChange.addEventListener("click", doIt);
