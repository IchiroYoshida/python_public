// Draw Ecli Equ lines in the sky.

function drawEcliEqu(ctx){
    // Draw equator.
    ctx.fillStyle = 'white'; 
    ctx.globalAlpha = 0.4;
 
    for (let deg = 0; deg <360; deg += 3){
        let equPoint = Astronomy.Horizon(date, observer, deg/15, 0, 'normal');
        az = equPoint.azimuth;
        alt = equPoint.altitude;
        if (alt >0){
            let dot = drawPolar(az, alt);
            ctx.save();
            ctx.translate(dot.x, dot.y);
            ctx.beginPath();
            ctx.fillRect(0,0,2,2);
            ctx.restore();
        }
    }
    // Draw ecliptic.
    /*
    ctx.fillStyle = 'yellow';
    for (let deg = 0; deg<360; deg += 3){
        rad = deg*Math.PI/180;
        x = Math.sin(rad);
        y = Math.cos(rad);
        z = 0;
        t = date; 
        const vec = new Astronomy.Vector(x, y, z, t);
        var ecli = Astronomy.Ecliptic(vec);

        lat = ecli.elat;
        lon = ecli.elon;
        console.log(deg,lon,lat);

        let ecliPoint = Astronomy.Horizon(date, observer, lon/15, lat ,'normal');
        azPoint = ecliPoint.azimuth;
        altPoint = ecliPoint.altitude;

        if (altPoint > 0);
        dot = drawPolar(azPoint,altPoint);
        ctx.save();
        ctx.translate(dot.x, dot.y);
        ctx.beginPath();
        ctx.fillRect(0,0,2,2);
        ctx.restore();
    }
    */
}

