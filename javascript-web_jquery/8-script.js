$.ajax({
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function (data) {
        const titleList = data["results"]
        for (titleIndex in titleList) {
            $("UL#list_movies").append('<li>' + titleList[titleIndex]["title"] + '</li>');
        }
    }
});
