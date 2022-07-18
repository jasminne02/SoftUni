function solve(array){
    let result = array
    .filter((num, idx) => idx % 2 != 0)
    .map(x=>x*2)
    .reverse();
    return result;
}

console.log(solve([10, 15, 20, 25]));
