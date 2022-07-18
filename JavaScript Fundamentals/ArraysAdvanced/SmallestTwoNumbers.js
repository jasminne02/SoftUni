function solve(array){
    let sortedArray = array.sort((a, b) => a-b);
    let result = sortedArray.slice(0, 2);
    return result.join(" ");
}

console.log(solve([30, 15, 2, 56]));
