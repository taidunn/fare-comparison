const searchBoxes = document.getElementsByClassName("search_box");
for (input of searchBoxes){
  autocomplete = new google.maps.places.Autocomplete(input, {});
};
