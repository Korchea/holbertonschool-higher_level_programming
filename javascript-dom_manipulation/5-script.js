toChange = document.querySelector("#update_header");
function doIt() {
    document.querySelector("header").innerHTML = "New Header!!!";
}
toChange.addEventListener("click", doIt);
