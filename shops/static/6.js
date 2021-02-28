

// // рисуем карту
// const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// const map = L.map('map', {
//     center: [49, 17],
//     zoom: 7
// })
//
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
//
// const shops = JSON.parse(document.getElementById('shops-data').textContent);
//
// console.log(shops);
//
// var minvalue = parseInt(minimumValue);
// var maxvalue = minvalue + 50;
//
// console.log("minvalue", minvalue);
// console.log("maxvalue", maxvalue);
//
//
// for (i in shops.features) {
//     var y = shops.features[i].properties.year;
//     console.log(y);
//     if (y < minimumValue || y > maximumValue) {
//         delete shops.features[i];
//         console.log('to delete')
//     }
//
// }
// // const filteredArray = shops.filter(x => x !== undefined);
// console.log(shops)
// var newShops = Object.values(shops.features).filter(x => x !== undefined);
// console.log(newShops);
//
// let feature = L.geoJSON(newShops).bindPopup(function (layer) {
//     return layer.feature.properties.name;
// }).addTo(map);
