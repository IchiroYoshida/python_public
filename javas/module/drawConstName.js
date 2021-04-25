// drawConstName.js 
function drawConstName(ctx){
    ctx.globalAlpha = 0.6;
    ctx.font = "9pt bold";
    ctx.fillStyle = '#8888FF';

    for(var con in ConstName){
	    var ra = Constellations[ConstName[con]].Ra/15;
	    var dec = Constellations[ConstName[con]].Dec;
      let hor = Astronomy.Horizon(date, observer, ra, dec, 'normal')
      var name = ConstName[con];
      var az = hor.azimuth;
      var alt = hor.altitude;

        if (alt>0) {
            let dot = drawPolar(az, alt);
            ctx.save();
            ctx.translate(dot.x,dot.y);
            ctx.fillText(name,0,0);
            ctx.restore();
        }
    }
    ctx.globalAlpha = 1.0;
}