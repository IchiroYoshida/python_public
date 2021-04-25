
// shape.js
function shape(ctx){
    rr = 200;
    alpha = 145.;
    var alphaRad = alpha * PI /180;

    /*
    ctx.fillStyle = '#330000';
    ctx.save();
    ctx.beginPath();
    ctx.arc(0, 0, rr, 0, PI*2,true);
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    */
   
    console.log('moon');

    let X = [];
    let Y = [];

    for (var th =-90; th < 100; th += 10){
        var rad = PI/180 * th;
        var x1 = rr * Math.cos(rad) * Math.cos(alphaRad);
        var y1 = rr * Math.sin(rad);
        X.push(x1);
        Y.push(y1);
    }
    
    for (var th =90; th > -100; th -= 10){
        var rad = PI/180 * th;
        var x2 = rr * Math.cos(rad);
        var y2 = rr * Math.sin(rad);
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
