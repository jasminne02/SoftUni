function solve(input){
    if (typeof input == 'number'){
        console.log((Math.PI * Number(input) * Number(input)).toFixed(2));
    } else { 
        console.log(`We can not calculate the circle area, because we receive a ${typeof input}.`)
    }
}

solve(2);
solve('not number');
