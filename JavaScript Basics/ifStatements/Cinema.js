function cinema(input){
    let movieType = input[0];
    let rows = Number(input[1]);
    let cols = Number(input[2]);
    let profit = 0;

    switch (movieType){
        case "Premier": profit = 12 * rows * cols; break;
        case "Normal": profit = 7.50 * rows * cols; break;
        case "Discount": profit = 5 * rows * cols; break;
    }

    console.log(`${(profit).toFixed(2)} leva`);
}

cinema(["Premier", "10", "12"]);
