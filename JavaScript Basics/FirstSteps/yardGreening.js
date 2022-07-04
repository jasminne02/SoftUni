function greening(input){
    let squareMetres = Number(input[0]);
    let sum = squareMetres * 7.61;
    let discount = sum * 0.18;
    sum -= discount;
    console.log(`The final price is: ${sum} lv.`);
    console.log(`The discount is: ${discount} lv.`)
}

greening([550]);
console.log();
greening([150]);
