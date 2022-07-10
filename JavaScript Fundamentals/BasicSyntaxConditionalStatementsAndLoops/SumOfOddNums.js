function solve(num){
    let sum = 0;
    for (let i = 1; num > 0; i += 2){
        console.log(i);
        sum += i;
        num -= 1;
    }

    console.log(`Sum: ${sum}`);
}


solve(5);
solve(3);
