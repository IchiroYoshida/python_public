// funcMoon.js

function funcMoon(date){
    var astroToday = new Astronomy.MakeTime(date);
    var prevMonth = astroToday.AddDays(-30);
    var previousNewMoon = Astronomy.SearchMoonPhase(0, prevMonth.date, 30);
    var MoonAge = astroToday.tt - previousNewMoon.tt; // Moon Age.
    var MA = MoonAge.toFixed(1);
    return(MA);
}
 