function solve(number){
    let firstNumber = String(number)[0];
    for (digit of String(number)){
        if (digit != firstNumber){
            console.log(false);
            return;
        }
    }
    console.log(true);
}

solve(2311);
solve(22222);
