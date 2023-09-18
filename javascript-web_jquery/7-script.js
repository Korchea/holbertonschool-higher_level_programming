$.ajax({
    url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    method: "GET",
    dataType: "json",
    success: function (data) {
        $("DIV#character").append(data["name"]);
    }
});
