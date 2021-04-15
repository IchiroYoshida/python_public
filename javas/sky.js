function draw() {
  const Radius = 640;
  const Clip = 300;
  var RadHalf = parseInt(Radius/2);
  var canvas = document.getElementById('stars');
  if (canvas.getContext){
    var ctx = canvas.getContext('2d');
  }
  ctx.fillRect(0,0,Radius,Radius);
  ctx.translate(RadHalf, RadHalf);

  // 円形のクリッピングパスを作成
  ctx.beginPath();
  ctx.arc(0,0,Clip,0,Math.PI*2,true);
  ctx.clip();

  // 背景を描く
  var lingrad = ctx.createLinearGradient(0,-RadHalf,0,RadHalf);
  lingrad.addColorStop(0, '#232256');
  lingrad.addColorStop(1, '#143778');

  ctx.fillStyle = lingrad;
  ctx.fillRect(-RadHalf,-RadHalf,Radius,Radius);

  // 星を描く
  for (var j=1;j<300;j++){
    ctx.save();
    ctx.fillStyle = '#fff';
    ctx.translate(RadHalf-Math.floor(Math.random()*Radius),
                  RadHalf-Math.floor(Math.random()*Radius));
    drawStar(ctx,Math.floor(Math.random()*4)+2);
    ctx.restore();
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
