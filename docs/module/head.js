//
const drawRadius2 = 640;
let drawRadius = parseInt(drawRadius2/2);
const drawClip = 300;

const PI = Math.PI;

// Location Fukuoka
const latitude = 33.594;
const longitude = 130.387;
const elevation = 20.0;
let observer = new Astronomy.Observer(latitude, longitude, elevation);

date = new Date();
console.log(date);

// BodyList of Solar system.
const BodyList = [
    'Mercury', 'Venus', 'Mars',
    'Jupiter', 'Saturn'
];   

// Position of the Sun.
let sun = Astronomy.Equator('Sun', date, observer, true, true);
let Sun_hor = Astronomy.Horizon(date, observer, sun.ra, sun.dec, 'normal');
let Sun_az =Sun_hor.azimuth;
let Sun_alt=Sun_hor.altitude;
console.log('Sun',Sun_az,Sun_alt);

// Position of the Moon.
let moon = Astronomy.Equator('Moon', date, observer, true, true);
let Moon_hor = Astronomy.Horizon(date, observer, moon.ra, moon.dec, 'normal');
let Moon_az =Moon_hor.azimuth;
let Moon_alt=Moon_hor.altitude;
console.log('Moon',Moon_az,Moon_alt);

// Milkyway 1000 clusters.
var Milkyway = Object.keys(Clusters);

// Hipparcos brightest 1000 stars.
var Stars = Object.keys(Hipparcos);

// The brightest 20 stars.
var Bright20Names = Object.keys(starName);

// Constellations.
var ConstName = Object.keys(Constellations);