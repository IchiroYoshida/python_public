
function polar(az, alt){
    let Az = az * (Math.PI/180);
    let Alt = alt * (Math.PI/180);

    let r = Math.PI/2 - Alt;
    let x =  -r * Math.sin(Az);
    let y =   r * Math.cos(Az);
    console.log(az,alt,x,y)
    return{x:x,y:y};
}

function drawCanvas(pos){
    const canvasRadius = 300;

    let XX = (2*pos.x/Math.PI)*canvasRadius;
    let YY = (2*pos.y/Math.PI)*canvasRadius;
    console.log(XX,YY);
    return{x:XX, y:YY};
}
