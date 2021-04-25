// drawMilkyway.js

function drawMilkyway(ctx){
    ctx.fillStyle = 'white';
    ctx.globalAlpha = 0.1;

    for(var mil in Milkyway){
	    var ra = Clusters[Milkyway[mil]].Ra/15;
	    var dec = Clusters[Milkyway[mil]].Dec;
        let hor = Astronomy.Horizon(date, observer, ra, dec, 'normal')
        az = hor.azimuth;
        alt = hor.altitude;

        if (alt>0) {
            let dot = drawPolar(az, alt);
            ctx.save();
            ctx.beginPath();
            ctx.arc(dot.x, dot.y, 3, 0, PI*2, false);
            ctx.fill();
            ctx.restore();
        }
    }
    ctx.globalAlpha = 1.0;
}