const latitude = 33.594;
const longitude = 130.387;
const elevation = 20.0;
let observer = new Astronomy.Observer(latitude, longitude, elevation);

date = new Date();
console.log(date);

const Hipparcos = {
    HIP32349:{Mag:-1.44,Ra:101.28854105,Dec:-16.71314306,BV: 0.009},
    HIP30438:{Mag:-0.62,Ra:95.98787763,Dec:-52.69571799,BV: 0.164},
    HIP69673:{Mag:-0.05,Ra:213.91811403,Dec:19.18726997,BV: 1.239},
    HIP71683:{Mag:-0.01,Ra:219.92041034,Dec:-60.83514707,BV: 0.710},
    HIP91262:{Mag: 0.03,Ra:279.23410832,Dec:38.78299311,BV:-0.001},
    HIP24608:{Mag: 0.08,Ra:79.17206517,Dec:45.99902927,BV: 0.795},
    HIP24436:{Mag: 0.18,Ra:78.63446353,Dec:-8.20163919,BV:-0.03},
    HIP37279:{Mag: 0.40,Ra:114.82724194,Dec:5.22750767,BV: 0.432},
    HIP7588:{Mag: 0.45,Ra:24.42813204,Dec:-57.23666007,BV:-0.158},
    HIP27989:{Mag: 0.45,Ra:88.79287161,Dec:7.40703634,BV: 1.500}
};

function polar(az, alt){
    let Az = az * (Math.PI/180);
    let Alt = alt * (Math.PI/180);

    let r = Math.PI - Alt;
    let x =  r * Math.sin(Az) + Math.PI;
    let y =  r * Math.cos(Az) + Math.PI;

    return{x:x,y:y};
}

function drawCanvas(pos){
    const canvasRadius = 320;
    const PI2 = Math.PI*2;

    let XX = (pos.x/PI2)*canvasRadius;
    let YY = (pos.y/PI2)*canvasRadius;
    return{x:XX, y:YY};

}

var Stars = Object.keys(Hipparcos);

for(var star in Stars){
	var ra = Hipparcos[Stars[star]].Ra/15;
	var dec = Hipparcos[Stars[star]].Dec;
	var mag = Hipparcos[Stars[star]].Mag;
	var bv = Hipparcos[Stars[star]].BV;
    let hor = Astronomy.Horizon(date, observer, ra, dec, 'normal')
    az = hor.azimuth;
    alt = hor.altitude;

    if (alt>0) {
        let pol  = polar(az, alt);
        console.log(az, alt, pol.x, pol.y);
        let dot  = drawCanvas(pol);
        console.log(az, alt, dot.x,dot.y);
    }
}
