
// shape.js
function shape(ctx){
    rr = 200;
    alpha = 151.927; //Moon phase;
    //alpha = alpha - 180;

    kai = 30 ;   // phase_angle;

    var alphaRad = alpha * PI /180;
    var kaiRad = kai * PI /180;

    console.log('moon phase angle:',kai);

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
    ctx.beginPath();
    ctx.moveTo(X[0],Y[0]);
    console.log('start:',X[0],Y[0])
    for (var i =1; i<len; i++){
        ctx.lineTo(X[i],Y[i]);
    }
    ctx.lineTo(X[0],Y[0]);
    ctx.fill();
}
