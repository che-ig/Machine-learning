function reduce(func, array, start=0) {
    const len = arr.length;
    let res = start
    for (index=0; index < len; index++) {
        res = func(res, array[index], index, arr);
        
    }
    return res
}

function forEach(func, arr, thisArg) {
    const len = arr.length;
    for (let index = 0; index < len; index++) {
        func.call(thisArg, arr[index], index, arr);
    }
}

function filter(func, arr, thisArg) {
    let newArr = [];
    const len = arr.length;
    let currRes;
    for (let index = 0; index < len; index++) {
        currRes = func.call(thisArg, arr[index], index, arr);
        if(currRes) {
            newArr.push(arr[index])
        }
    }
    return newArr;
}

function map(func, arr, thisArg) {
    let newArr = [];
    const len = arr.length;
    for (let index = 0; index < len; index++) {
        newArr.push(func.call(thisArg, arr[index]));
    }
    return newArr;
}

function some(func, arr, thisArg) {
    const len = arr.length;
    let res = false;
    for (let index = 0; index < len; index++) {
        res = func.call(thisArg, arr[index]);
        if(res) {
            break;
        }
    }
    return res;
}
function evry(func, arr, thisArg) {
    const len = arr.length;
    let res = false;
    for (let index = 0; index < len; index++) {
        res = func.call(thisArg, arr[index]);
        if(!res) {
            break;
        }
    }
    return res;
}

function my(a, b) {
    return a * b;
}

function my_2(a) {
    return a * 2;
}

function my_3(a) {
    return a > 3;
}

arr = [1, 2, 3, 4, 5, 6]
console.log(reduce(my, arr, null));
console.log(forEach(my_2, arr));
console.log(map(my_2, arr));
console.log(filter(my_3, arr));
console.log(some(my_3, arr));
console.log(evry(my_3, arr));
arr.reduce(my, null)