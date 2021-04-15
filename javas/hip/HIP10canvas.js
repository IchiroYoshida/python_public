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

    let r = Math.PI/2 - Alt;
    let x =  -r * Math.sin(Az);
    let y =   r * Math.cos(Az);
    console.log(az,alt,x,y)
    return{x:x,y:y};
}

function drawCanvas(pos){
    const canvasRadius = 320;

    let XX = (1 + 2*pos.x/Math.PI)*canvasRadius;
    let YY = (1 + 2*pos.y/Math.PI)*canvasRadius;
    console.log(XX,YY);
    return{x:XX, y:YY};

}

var Stars = Object.keys(Hipparcos);

function drawSky(){
    const Radius2 = 640;
    const Clip = 300;
    var Radius = parseInt(Radius2/2);
    var canvas = document.getElementById('stars');
    if (canvas.getContext){
        var ctx = canvas.getContext('2d');
    }
    ctx.fillRect(0,0,Radius2, Radius2);
    ctx.translate(Radius, Radius);

    // 円形のクリッピングパスを作成
    ctx.beginPath();
    ctx.arc(0, 0, Clip,0,Math.PI*2,true);
    ctx.clip();

    //　背景を描く
    var lingrad = ctx.createLinearGradient(0,-Radius,0,Radius);
    lingrad.addColorStop(0, '#232256');
    lingrad.addColorStop(1, '#143778');

    ctx.fillStyle = lingrad;
    ctx.fillRect(-Radius,-Radius,Radius2,Radius2);

    drawStarsInTheSky(ctx,Stars);
}

function drawStarsInTheSky(ctx,Stars){
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
            let dot  = drawCanvas(pol);
            ctx.save();
            ctx.fillStyle = '#fff';
            ctx.translate(dot.x,dot.y);
            let r = (5-mag)**1.5/5;
            console.log(r)
            drawStar(ctx,r);
            ctx.restore();
        }
    }
}


function drawStar(ctx,r){
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(r,0);
    for (var i=0;i<9;i++){
      ctx.rotate(Math.PI/5);
      if(i%2 === 0) {
        ctx.lineTo((r/0.525731)*0.200811,0);
      } else {
        ctx.lineTo(r,0);
      }
    }
    ctx.closePath();
    ctx.fill();
    ctx.restore();
}