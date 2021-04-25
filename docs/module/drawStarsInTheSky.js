// drawStarsInTheSky.js 
function drawStarsInTheSky(ctx){
    ctx.font = "8pt bold";
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
            ctx.save();
            ctx.fillStyle = bv;
            ctx.translate(dot.x,dot.y);
            let r = (5-mag)**1.5/1.5;
            drawStar(ctx,r);
            // Names of the brightest 20 stars.
            var name = starName[Stars[star]];
            if(name){
              ctx.fillText(name,0,0);
            }
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