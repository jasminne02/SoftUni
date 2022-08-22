function solve(arrayOfFlavors, firstFlavor, secondFlavor){
    let newArray = [];
    let start = false;
    for (let flavor of arrayOfFlavors){
        if (start){
            newArray.push(flavor);
        }
        if (flavor == firstFlavor) {
            newArray.push(flavor);
            start = true;
        } else if (flavor == secondFlavor) {
            newArray.push(flavor);
            start = false;
        }
    }

    return newArray;
}

console.log(solve(['Pumpkin Pie','Key Lime Pie','Cherry Pie','Lemon Meringue Pie','Sugar Cream Pie'],'Key Lime Pie','Lemon Meringue Pie'))
