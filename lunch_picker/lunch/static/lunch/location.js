let lat = document.getElementById("lat");
let lng = document.getElementById("lng");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(fillInPosition);
  } else {
    // very temporary error handling
    lat.value = "Geolocation is not supported by this browser.";
  }
}

function fillInPosition(position) {
  lat.value = position.coords.latitude;
  lng.value = position.coords.longitude;
}
