/* 2 question 11 sprint */

const howMuchSec = (sec=0, min=0, h=0, d=0, w=0, m=0, y=0) => {
    let minute = 60, hour = minute*60, day = hour*24, week = day*7, 
    month = day*30, year = day*365;
    let result = sec + min*minute + h*hour + d*day + w*week + m*month + y*year;
    return result;
}

	
console.log(howMuchSec(12, 3));