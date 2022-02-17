/* 1 question 11 sprint */

const filterNums = (arr, num=0, param='greater') => {
    let newArr = arr.filter(number => number > num);
    if(param == 'less'){
        newArr = arr.filter(number => number < num);
    }
    return newArr;
};