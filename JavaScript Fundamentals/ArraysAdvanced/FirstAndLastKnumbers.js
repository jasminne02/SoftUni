function solve(array){
    let kNumber = Number(array.shift());
    let length = array.length;

    let firstArr = array.slice(0, kNumber);
    let lastArr = array.slice(length-kNumber, length);
    
    console.log(firstArr.join(" "));
    console.log(lastArr.join(" "));
}

solve([2, 7, 8, 9]);
console.log();
solve([3, 6, 7, 8, 9]);
