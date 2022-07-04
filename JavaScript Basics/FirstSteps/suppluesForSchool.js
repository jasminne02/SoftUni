function supplies(input){
    let pens = Number(input[0]) * 5.80;
    let markers = Number(input[1]) * 7.20;
    let cleanerLitres = Number(input[2]) * 1.20;
    let discount = Number(input[3]) * 0.01;
    let total = pens + markers + cleanerLitres;
    total -= total * discount;
    console.log(total);
}

supplies(["2 ","3 ","4 ", "25 "]);
supplies([4, 2, 5, 13]);
