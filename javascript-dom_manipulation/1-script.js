const toChange = document.querySelector("#red_header");
function doit() {
    toChange.style.color = "#FF0000";
}
toChange.addEventListener("click", doit);
