'use strict';
const size = 200;

const
    pi = Math.PI,
    pi2 = pi * 2,
    topAngle = pi + pi / 2 * 3,
    bottomAngle = pi + pi / 2,
    halfSize = size / 2,

    c = [],
    ctx = [],
    start = [0, topAngle, 0],
    end = [pi2, bottomAngle, pi2];

window.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.moonAge').style.height = `${size}px`;
    document.querySelector('.d').style.width = `${size}px`;
    for(let i = 0; i < 3; i++) {
        c[i] = document.getElementById(`a${i}`);
        c[i].style.width = `${size}px`;
        c[i].style.height = `${size}px`;
        c[i].width = size;
        c[i].height = size;
        ctx[i] = c[i].getContext('2d');
        ctx[i].fillStyle = i === 0 ? '#444444' : '#ffff00';
        ctx[i].arc(halfSize, halfSize, halfSize * .95, start[i], end[i]);
        ctx[i].fill();
    }
    const e = document.querySelector('#c');
    e.value = new Date().toLocaleDateString('sv');
    chg(e.value);
}, false);

function chg(d){
    const date = new Date(d);
    if(isNaN(date.getTime())) return;
    date.setHours(12);

    const day = date.getTime() / 864e5 - 6.475,
          // 平均朔望月
          r = 29.530588853 +
                2.162e-9 * ((date.getTime() - 946727935816) / 315576e5),
          age = day > 0 ? day % r : (r + day % r) % r;
    console.log(age,date,day,date.getTime())

    document.querySelector('#disp').innerHTML =
        `${date.toLocaleDateString()}<br>月齢:${age.toFixed(1)}`;
    appearance(age, r);
}

function appearance(age, m) {
    const s  = Math.cos(pi2 * age / m),
          s2 = Math.sin(pi2 * age / m),
          r  = Math.abs(halfSize * s);
    c[1].style.transform = `rotate(${s2 > 0 ? 180 : 0}deg)`;
    ctx[2].clearRect(0, 0, size, size);
    ctx[2].beginPath();
    ctx[2].fillStyle = s > 0 ? '#444444' : '#ffff00';
    ctx[2].arc(halfSize, halfSize, halfSize * .95, 0, pi2);
    ctx[2].fill();
    c[2].style.width = `${r * 2}px`;
    c[2].style.left = `${halfSize - r}px`;
}
