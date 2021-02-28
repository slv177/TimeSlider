const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {
    center: [49, 17],
    zoom: 7
})
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const shops = JSON.parse(document.getElementById('shops-data').textContent);
const links = JSON.parse(document.getElementById('links-data').textContent);
let featurelinks = L.geoJSON(links).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
let feature = L.geoJSON(shops).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
// map.fitBounds(feature.getBounds(), { padding: [100, 100] });