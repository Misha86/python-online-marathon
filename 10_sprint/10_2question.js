/* 2 question 10 sprint */


function combineArray(arr1, arr2) {
    let  arr1New = arr1.filter(element => (typeof element) === 'number');
    let  arr2New = arr2.filter(element => (typeof element) === 'number');
    return arr1New.concat(arr2New);
}



