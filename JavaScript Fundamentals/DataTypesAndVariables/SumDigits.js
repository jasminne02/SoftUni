function solve(number){
    let sum = 0;
    let len = String(number).length;

    for (let idx = 0; idx < len; idx++){
        sum += Number(number) % 10;
        number = parseInt( Number(number) / 10);
    }

    console.log(sum);
}


solve(245678);
