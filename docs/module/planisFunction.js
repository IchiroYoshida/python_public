//planisFunction.js
function drawPolar(az, alt){
    let Az = az * (PI/180);
    let Alt = alt * (PI/180);

    let r = PI/2 - Alt;
    let x =  -r * Math.sin(Az);
    let y =  -r * Math.cos(Az);
    let XX = 2*x/PI*drawRadius;
    let YY = 2*y/PI*drawRadius;
    //console.log(XX, YY);
    return{x:XX, y:YY};
}
