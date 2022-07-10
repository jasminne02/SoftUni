function round(number, precision){ 

    if (precision > 15){
        precision = 15;
    }

    let roundedNumber = Number(number).toFixed(precision);

    console.log(parseFloat(roundedNumber));
}


round(3.30000000789, 4);
