// var geocoder = new google.maps.Geocoder();
var fromGeocode = ""

document.getElementById('go').addEventListener('click', function() {
  var fromAdd = document.getElementById('from').value;
  geocoder.geocode({'from': fromAdd}, function(results, status){
    if (status === 'OK'){
      fromGeocode = result[0];
      console.log(fromGeocode);
    } else{
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
});
