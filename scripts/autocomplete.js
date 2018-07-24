// Create the search box and link it to the UI element.
// var input = document.getElementById('pac-input');
// var searchBox = new google.maps.places.SearchBox(input);
const searchBoxes = document.getElementsByClassName("search_box");
for (input of searchBoxes){
  var searchBox = new google.maps.places.SearchBox(input);
};
