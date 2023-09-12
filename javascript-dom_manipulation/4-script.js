toChange = document.querySelector("#add_item");
function doIt() {
    document.querySelector(".my_list").innerHTML += "<li>Item</li>";
}
toChange.addEventListener("click", doIt);
