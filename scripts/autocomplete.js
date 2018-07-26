const options = {country: "us"};
const fromAddress = document.getElementById("from_address");
const acFromAddress = new google.maps.places.Autocomplete(fromAddress, options);
const toAddress = document.getElementById("to_address");
const acToAddress = new google.maps.places.Autocomplete(toAddress, options);
const address_form = document.getElementById("address_form");

const form = document.getElementById("address_form");
form.addEventListener("keypress", function(e){
  if(e.keyCode == 13){
    e.preventDefault()
  };
});
