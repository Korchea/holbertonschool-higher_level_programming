toChange = document.querySelector(header);
function doit() {
    toChange.style.color = "#FF0000";
}
toChange.forEach(header => {
    toChange.addEventListener("click", doit);
});
