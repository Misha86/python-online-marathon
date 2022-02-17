/* 4 question 11 sprint */

const sumOfLen = (...words) => {
    let result = words ? words.reduce((total, word) => total + word.length, 0): 0;
    return result;
}

	
console.log(sumOfLen('hello', 'hi'));
console.log(sumOfLen());