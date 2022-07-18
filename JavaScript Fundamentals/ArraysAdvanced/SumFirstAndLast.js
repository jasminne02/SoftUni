function sum(array){
    let first = Number(array.shift());
    let last = Number(array.pop());
    return first + last;
}

console.log(sum(['20', '30', '40']));
