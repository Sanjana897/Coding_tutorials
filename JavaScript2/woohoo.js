function runThatQuery() {
	console.log ("This function is really working!");
	
	var baseUrl = "http://www.omdbapi.com/?";
	var searchQuery = $( "#movieTitleID" ).val();

	
	$.ajax({
        url: baseUrl + '&s=' + encodeURI(searchQuery),
        dataType: "jsonp",
        success: searchCallback
    });
               
    }
	
function searchCallback(data) {
	console.log ("This Ajax stuff works");
	console.log (JSON.stringify(data));
	$("#movieForm").html('I found ' + data.totalResults + ' results total! <br>');
	
	var movies = data.Search;
	$.each(movies, function(index, movie) {
        $("#movieForm").append('<h3>' + movie.Title + '</h3><img src="' + movie.Poster + '">');
        
});
}
