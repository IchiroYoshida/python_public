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
var Stars = Object.keys(Hipparcos);

function drawPolar(az, alt){
    let Az = az * (PI/180);
    let Alt = alt * (PI/180);

    let r = PI/2 - Alt;
    let x =  -r * Math.sin(Az);
    let y =  -r * Math.cos(Az);
    let XX = 2*x/PI*drawRadius;
    let YY = 2*y/PI*drawRadius;
    //console.log(XX, YY);
    return{x:XX, y:YY};
}

function drawSky(){
    var canvas = document.getElementById('stars');
    if (canvas.getContext){
        var ctx = canvas.getContext('2d');
    }
    ctx.fillRect(0,0,drawRadius2, drawRadius2);
    ctx.translate(drawRadius, drawRadius);

    // 円形のクリッピングパスを作成
    ctx.beginPath();
    ctx.arc(0, 0, drawClip,0,PI*2,true);
    ctx.clip();

    //　背景を描く
    var lingrad = ctx.createLinearGradient(0,-drawRadius,0,drawRadius);
    lingrad.addColorStop(0, '#232256');
    lingrad.addColorStop(1, '#143778');

    ctx.fillStyle = lingrad;
    ctx.fillRect(-drawRadius,-drawRadius,drawRadius2,drawRadius2);

    drawStarsInTheSky(ctx,Stars);
}

function bv2rgb(bv){
    if (bv < -0.4){
        bv = -0.4;
    } else if (bv > 2.0){
        bv = 2.0;
    }

    if (( bv >= -0.40) && ( bv<0.00)){
        var t=(bv+0.40)/(0.00+0.40);
        var r=0.61+(0.11*t)+(0.1*t*t);
    } else if (( bv >= 0.00) && (bv<0.40)) {
        var t=(bv-0.00)/(0.400-0.00);
        var r=0.83+(0.17*t);
    } else if (( bv >= 0.40) && (bv<2.10)) {
        var t=(bv-0.40)/(2.10-0.40);
        var r=1.00;
    }
    if (( bv >= -0.40) && (bv <0.00)) {
        var t=(bv+0.40)/(0.00+0.40);
        var g=0.70+(0.07*t)+(0.1*t*t);
    } else if (( bv >= 0.00) && ( bv<0.40)) {
        var t=(bv-0.00)/(0.40-0.00);
        var g=0.87+(0.11*t);
    } else if (( bv >= 0.40) && (bv<1.60)){
        var t=(bv-0.40)/(1.60-0.40);
        var g=0.98-(0.16*t);
    } else if (( bv>= 1.60) && (bv<2.00)){
        var t=(bv-1.60)/(2.00-1.60);
        var g=0.82-(0.5*t*t);
    }

    if ((bv>=-0.40)&&(bv<0.40)){
        var t=(bv+0.40)/(0.40+0.40);
        var b=1.00;
    } else if ((bv>=0.40)&&(bv<1.50)){
        var t=(bv-0.40)/(1.50-0.40);
        var b=1.00-(0.47*t)+(0.1*t*t);
    } else if ((bv>=1.50)&&(bv<1.94)){
        var t=(bv-1.50)/(1.94-1.50);
        var b=0.63 - (0.6*t*t);
    }
    console.log('Table',r,g,b)
}

function srgb(c){
    return( ( c <= 0.0031308) ? 12.92 * c : ((1 + 0.055) * c**(1/2.4) - 0.055));
}

function BVcolor(bv){
    // Sekiguchi & Fukugita (2000)
    const C =[3.939654, -0.395361, 0.2082113, -0.0604097];
    let logT = C[0] + C[1]*bv + C[2]*bv*bv + C[3]*bv*bv*bv;
    let TT = 10**logT;

    // Planckian locus
    if (TT < 4000){
        var x = -0.2661239e+9 / (TT*TT*TT) 
                -0.2343580e+6 / (TT*TT)
                +0.8776956e+3 / TT
                +0.179910;
    } else {
        var x = -3.0258469e+9 / (TT*TT*TT)
                +2.1070379e+6 / (TT*TT)
                +0.2226347e+3 / TT
                +0.240390;
    }

    if (TT < 2222) {
        var y = -1.1063814  * x*x*x
                -1.34811020 * x*x
                +2.18555832 * x
                -0.20219683;
    } else if (TT < 4000) {
        var y = -0.9549476  * x*x*x
                -1.37418593 * x*x
                +2.09137015 * x
                -0.16748867;
    } else {
        var y =  3.0817580 * x*x*x
                -5.87338670 * x*x
                +3.75112997 * x
                -0.37001483;
    }
    let Y = 1.0;
    let X = Y * x / y;
    let Z = Y * (1.0 - x - y )/Y;

    let r = srgb( 3.2406 * X - 1.5372 * Y - 0.4986 * Z);
    let g = srgb(-0.9689 * X + 1.8758 * Y + 0.0415 * Z);
    let b = srgb( 0.0557 * X - 0.2040 * Y + 1.0570 * Z);
    console.log('rgb',r,g,b);

    let R = parseInt((r < 0 ? 0 : (r > 1 ? 1: r)) *255);
    let G = parseInt((g < 0 ? 0 : (g > 1 ? 1: g)) *255);
    let B = parseInt((b < 0 ? 0 : (b > 1 ? 1: b)) *255);

    RR = R.toString(16);
    GG = G.toString(16);
    BB = B.toString(16);

    //console.log('BV=',RR,GG,BB);
    BVcol = '#'+RR+GG+BB
    //console.log(BVcol);
    return(BVcol);
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
            let dot = drawPolar(az, alt);
            let BVcol = BVcolor(bv);
            bv2rgb(bv);
            console.log(BVcol);
            ctx.save();
            //ctx.fillStyle = '#fff';
            ctx.fillStyle = BVcol;
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