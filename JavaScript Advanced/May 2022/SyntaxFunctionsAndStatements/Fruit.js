function solve(fruit, grams, pricePerKg){
    let price = grams * pricePerKg;
    console.log(`I need $${(price/1000).toFixed(2)} to buy ${(grams/1000).toFixed(2)} kilograms ${fruit}.`);
}

solve('orange', 2500, 1.80);
