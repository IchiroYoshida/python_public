// drawPlanets.js

function drawPlanets(ctx){
    ctx.font = "12px bold";
    ctx.fillStyle = 'red';

    for (let body of BodyList) {
        let equ_ofdate = Astronomy.Equator(body, date, observer, true, true);
        let hor = Astronomy.Horizon(date, observer, equ_ofdate.ra, equ_ofdate.dec, 'normal');
        let az=hor.azimuth;
        let alt=hor.altitude;
        
        if (alt>0) {
            let dot = drawPolar(az, alt);
            ctx.save();
            ctx.beginPath();
            ctx.arc(dot.x, dot.y,3 ,0, Math.PI*2, false);
            ctx.fill();
            // Name of the Planets.
            ctx.fillText(body,dot.x, dot.y);
            ctx.restore();
        }
    }
}
