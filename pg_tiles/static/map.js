var map = L.map('map').setView([46.06, 11.12], 10);
L.tileLayer('http://{s}.tiles.mapbox.com/v3/redshadow.j99f50fg/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18
}).addTo(map);
