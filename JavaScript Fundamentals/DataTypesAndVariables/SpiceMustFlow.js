function solve(startingYield){
    startingYield = Number(startingYield);
    let days = 0;
    let toatalAmount = 0;
    
    while (startingYield >= 100){
        toatalAmount += startingYield;
        toatalAmount -= 26;
        days += 1;
        startingYield -= 10;
    }

    toatalAmount -= 26;

    console.log(days);
    console.log(toatalAmount);
}


solve(111);
console.log();
solve(450);
