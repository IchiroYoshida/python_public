// drawPlanets.js

function drawPlanets(ctx){
    for (let body of BodyList) {
        let equ_ofdate = Astronomy.Equator(body, date, observer, true, true);
        let hor = Astronomy.Horizon(date, observer, equ_ofdate.ra, equ_ofdate.dec, 'normal');
        let az=hor.azimuth;
        let alt=hor.altitude;
        //console.log(body,az,alt);
        
        if (alt>0) {
            let dot = drawPolar(az, alt);
            //console.log(body,dot);
            ctx.save();
            ctx.fillStyle = '#FF0000'; //Red
            ctx.beginPath();
            ctx.arc(dot.x, dot.y,3 ,0, Math.PI*2, false);
            ctx.fill();
            ctx.restore();
        }
    }
}
