/* 3 question 11 sprint */

const maxInterv = (...numbers) => {
    let result = 0;
    numbers.reduce((previousNumber, currentNumber) => {
        let interv = Math.abs(previousNumber - currentNumber);
        result = interv > result ? interv: result;
        return currentNumber;
    });
    return result;
}

	
console.log(maxInterv(12, 3, 4, -9));