const mapTo = document.getElementById("to");
const mapFrom = document.getElementById("from");

console.log(mapTo);
console.log(mapFrom)
// for (input of mapTo){
//
// };
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 2
    // origin: mapFrom
    // destination: mapTo
  });
}
