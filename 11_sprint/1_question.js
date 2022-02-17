/* 1 question 11 sprint */

const filterNums = (arr, number=0, param='greater') => {
    let nArr = arr.filter(num => (param == 'less') ? num < number: num > number);
    return nArr;
};
