// drawMoon.js

function drawMoon(ctx){
    rr = 10;  //Moon radius.
    ctx.globalAlpha = 1.0;

    var date0 = date;
    astroToday = new Astronomy.MakeTime(date);
    date0.setMonth(date0.getMonth() - 1);
    var previousNewMoon = Astronomy.SearchMoonPhase(0, date0, 30);
    var MoonAge = astroToday.tt - previousNewMoon.tt; // Moon Age.
    var MA = MoonAge.toFixed(1);
    var phase = Astronomy.MoonPhase(date); //Moon phase;
    var moonIllumi = new Astronomy.Illumination("Moon",date);
    var pAngle = moonIllumi.phase_angle;　//phase_angle;
    var alphaRad = phase * PI /180;
    var kaiRad = pAngle * PI /180;

    let X = [];
    let Y = [];

    for (var th =-90; th < 100; th += 10){
        var rad = PI/180 * th;
        var x0 = Math.cos(rad) * Math.cos(alphaRad);
        var y0 = Math.sin(rad);
        var x1 = Math.cos(kaiRad)*x0 - Math.sin(kaiRad)*y0;
        var y1 = Math.sin(kaiRad)*x0 + Math.cos(kaiRad)*y0;
        var x2 = rr * x1 ;
        var y2 = rr * y1 ;
        X.push(x2);
        Y.push(y2);
    }
    
    for (var th =90; th > -100; th -= 10){
        var rad = PI/180 * th;
        var x0 =  Math.cos(rad);
        var y0 =  Math.sin(rad);
        var x1 =  Math.cos(kaiRad)*x0 - Math.sin(kaiRad)*y0;
        var y1 =  Math.sin(kaiRad)*x0 + Math.cos(kaiRad)*y0;
        var x2 = rr * x1 ;
        var y2 = rr * y1 ;
        X.push(x2);
        Y.push(y2);
    }
    var len = X.length;
    
    ctx.fillStyle = '#FFFFFF';
    ctx.save();
    let dot = drawPolar(Moon_az, Moon_alt);
    ctx.fillStyle = 'yellow';
    ctx.font = '12px bold';
    ctx.beginPath();
    ctx.translate(dot.x,dot.y);
    ctx.moveTo(X[0],Y[1]);
    //console.log('start:',X[0],Y[0])
    for (var i =1; i<len; i++){
        ctx.lineTo(X[i],Y[i]);
    }
    ctx.lineTo(X[0],Y[0]);
    ctx.fill();
    ctx.restore();

    // draw MA text.
    ctx.fillStyle = 'white';
    ctx.font = '15pt bold';
    ctx.save();
    ctx.beginPath();
    ctx.beginPath();
    ctx.translate(dot.x, dot.y)
    ctx.fillText(MA, 0, 0);
    ctx.restore();
}