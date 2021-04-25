// drawSky.js
function drawSky(){
    var canvas = document.getElementById('stars');
    if (canvas.getContext){
        var ctx = canvas.getContext('2d');
    }
    ctx.fillRect(0,0,drawRadius2, drawRadius2);
    ctx.translate(drawRadius, drawRadius);

    // 円形のクリッピングパスを作成
    ctx.beginPath();
    ctx.arc(0, 0, drawClip,0,PI*2,true);
    ctx.clip();

    //　背景を描く
    var lingrad = ctx.createLinearGradient(0,-drawRadius,0,drawRadius);
    lingrad.addColorStop(0, '#232256');
    lingrad.addColorStop(1, '#143778');

    ctx.fillStyle = lingrad;
    ctx.fillRect(-drawRadius,-drawRadius,drawRadius2,drawRadius2);

    drawMilkyway(ctx); //draw Milkyway 1000 clusters.
    drawStarsInTheSky(ctx);  //draw Hipparcos 1000 stars.
    drawPlanets(ctx); //draw planets.
    drawEcliEqu(ctx); //draw Ecli. Equ. lines.
    drawMoon(ctx); //draw Moon.
    drawConstName(ctx); //draw constellation names.
}