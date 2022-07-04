function calculator(input){
    let depositSum = Number(input[0]);
    let depositPeriod = Number(input[1]);
    let anualPercent = Number(input[2]) * 0.01;
    let final = depositSum + depositPeriod * ((depositSum*anualPercent)/12);
    console.log(final);
}

calculator([200, 3, 5.7])
calculator([2350, 6, 7])
