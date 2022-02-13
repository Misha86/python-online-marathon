/* 4 question 10 sprint */


function factorial(n) {
    let total = 1;
    for(let i=1;n>=i;i++){
        total *= i;
    }
    return total;
}

function processArray(arr, factorial) {
    let factorialArr = arr.map(factorial);
    return factorialArr;
}