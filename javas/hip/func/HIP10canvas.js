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
    HIP27989:{Mag: 0.45,Ra:88.79287161,Dec:7.40703634,BV: 1.500},
    HIP68702:{Mag: 0.61,Ra:210.95601898,Dec:-60.3729784,BV:-0.231},
    HIP97649:{Mag: 0.76,Ra:297.6945086,Dec:8.86738491,BV: 0.221},
    HIP60718:{Mag: 0.77,Ra:186.64975585,Dec:-63.09905586,BV:-0.243},
    HIP21421:{Mag: 0.87,Ra:68.98000195,Dec:16.50976164,BV: 1.538},
    HIP65474:{Mag: 0.98,Ra:201.2983523,Dec:-11.16124491,BV:-0.235},
    HIP80763:{Mag: 1.06,Ra:247.35194804,Dec:-26.43194608,BV: 1.865},
    HIP37826:{Mag: 1.16,Ra:116.33068263,Dec:28.02631031,BV: 0.991},
    HIP113368:{Mag: 1.17,Ra:344.41177323,Dec:-29.62183701,BV: 0.145},
    HIP62434:{Mag: 1.25,Ra:191.93049537,Dec:-59.68873246,BV:-0.238},
    HIP102098:{Mag: 1.25,Ra:310.3579727,Dec:45.28033423,BV: 0.092},
    HIP71681:{Mag: 1.35,Ra:219.91412833,Dec:-60.83947139,BV: 0.900},
    HIP49669:{Mag: 1.36,Ra:152.09358075,Dec:11.96719513,BV:-0.087},
    HIP33579:{Mag: 1.50,Ra:104.65644451,Dec:-28.97208931,BV:-0.211},
    HIP36850:{Mag: 1.58,Ra:113.65001898,Dec:31.88863645,BV: 0.034},
    HIP61084:{Mag: 1.59,Ra:187.79137202,Dec:-57.11256922,BV: 1.600},
    HIP85927:{Mag: 1.62,Ra:263.40219373,Dec:-37.10374835,BV:-0.231},
    HIP25336:{Mag: 1.64,Ra:81.28278416,Dec:6.34973451,BV:-0.224},
    HIP25428:{Mag: 1.65,Ra:81.57290804,Dec:28.60787346,BV:-0.13},
    HIP45238:{Mag: 1.67,Ra:138.30100329,Dec:-69.71747245,BV: 0.070},
    HIP26311:{Mag: 1.69,Ra:84.05338572,Dec:-1.20191725,BV:-0.184},
    HIP109268:{Mag: 1.73,Ra:332.05781838,Dec:-46.96061593,BV:-0.07},
    HIP26727:{Mag: 1.74,Ra:85.18968672,Dec:-1.94257841,BV:-0.199},
    HIP39953:{Mag: 1.75,Ra:122.38314727,Dec:-47.33661177,BV:-0.145},
    HIP62956:{Mag: 1.76,Ra:193.5068041,Dec:55.95984301,BV:-0.022},
    HIP90185:{Mag: 1.79,Ra:276.04310967,Dec:-34.3843146,BV:-0.031},
    HIP15863:{Mag: 1.79,Ra:51.08061889,Dec:49.86124281,BV: 0.481},
    HIP54061:{Mag: 1.81,Ra:165.93265365,Dec:61.75111888,BV: 1.061},
    HIP34444:{Mag: 1.83,Ra:107.09785853,Dec:-26.39320776,BV: 0.671},
    HIP67301:{Mag: 1.85,Ra:206.8856088,Dec:49.31330288,BV:-0.099},
    HIP41037:{Mag: 1.86,Ra:125.62860299,Dec:-59.50953829,BV: 1.196},
    HIP86228:{Mag: 1.86,Ra:264.32969072,Dec:-42.99782155,BV: 0.406},
    HIP28360:{Mag: 1.90,Ra:89.88237261,Dec:44.94743492,BV: 0.077},
    HIP82273:{Mag: 1.91,Ra:252.16610742,Dec:-69.02763503,BV: 1.447},
    HIP42913:{Mag: 1.93,Ra:131.17582214,Dec:-54.70856797,BV: 0.043},
    HIP31681:{Mag: 1.93,Ra:99.42792641,Dec:16.39941482,BV: 0.001},
    HIP100751:{Mag: 1.94,Ra:306.41187347,Dec:-56.73488071,BV:-0.118},
    HIP11767:{Mag: 1.97,Ra:37.94614689,Dec:89.26413805,BV: 0.636},
    HIP30324:{Mag: 1.98,Ra:95.6749475,Dec:-17.95591658,BV:-0.24},
    HIP46390:{Mag: 1.99,Ra:141.8968826,Dec:-8.65868335,BV: 1.440},
    HIP50583:{Mag: 2.01,Ra:154.99234054,Dec:19.84186032,BV: 1.128},
    HIP9884:{Mag: 2.01,Ra:31.79285757,Dec:23.46277743,BV: 1.151}
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
    const canvasRadius = 300;

    let XX = (2*pos.x/Math.PI)*canvasRadius;
    let YY = (2*pos.y/Math.PI)*canvasRadius;
    console.log(XX,YY);
    return{x:XX, y:YY};
}

var Stars = Object.keys(Hipparcos);

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
            let pol  = polar(az, alt);
            let dot  = drawCanvas(pol);
            ctx.save();
            ctx.fillStyle = '#fff';
            ctx.translate(dot.x,dot.y);
            let r = (5-mag)**1.5/5;
            console.log(r);
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