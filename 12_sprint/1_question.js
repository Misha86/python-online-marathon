/* 1 question 12 sprint */
    
function getMin(arr) {
    // return arr.reduce((min, number) => min > number? number: min);
    // return Math.min(...arr);
    return Math.min.apply(null, arr);
}

console.log(getMin([12, 6, 22, 13, 7]))