function solve(products){
    let productsSorted = products.sort();
    let productsResult = [];

    for (let idx=0; idx<productsSorted.length; idx++){
        productsResult.push(`${idx+1}.${productsSorted[idx]}`);
    }

    return productsResult.join(" ");
}

console.log(solve(["Orange", "Apple", "Kiwi", "Banana"]));
