const latitude = 33.594;
const longitude = 130.387;
const elevation = 20.0;
let observer = new Astronomy.Observer(latitude, longitude, elevation);

date = new Date();
console.log(date);
var Stars = Object.keys(Hipparcos);

function drawPolar(az, alt){
    const canvasRadius = 300;
    let Az = az * (Math.PI/180);
    let Alt = alt * (Math.PI/180);

    let r = Math.PI/2 - Alt;
    let x =  -r * Math.sin(Az);
    let y =  -r * Math.cos(Az);
    let XX = 2*x/Math.PI*canvasRadius;
    let YY = 2*y/Math.PI*canvasRadius;
    //console.log(XX, YY);
    return{x:XX, y:YY};
}

//var Stars = Object.keys(Hipparcos);

function drawSky(){
    const Radius2 = 640;
    const Clip = 320;
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
            //let pol  = polar(az, alt);
            //let dot  = drawCanvas(pol);
            let dot = drawPolar(az, alt);
            ctx.save();
            ctx.fillStyle = '#fff';
            ctx.translate(dot.x,dot.y);
            let r = (5-mag)**1.5/2;
            //console.log(r);
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