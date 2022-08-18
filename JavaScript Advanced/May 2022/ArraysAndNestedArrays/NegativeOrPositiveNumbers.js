function solve(array){
    array = array.map(Number);
    let firstPart = [];
    let secondPart = [];

    while(array.length > 0){
        let minElement = Math.min.apply(Math, array);
        let maxElement = Math.max.apply(Math, array);
        array = remove(array, minElement);
        array = remove(array, maxElement);
        firstPart.push(minElement);
        secondPart.unshift(maxElement);
    }

    let orderedArray = firstPart.concat(secondPart);
    for (let element of orderedArray){
        console.log(element);
    }
}

function remove(array, element){
    let newArray = [];
    for (let el of array){
        if (el != element){
            newArray.push(el);
        }
    }
    return newArray;
}

solve([7, -2, 8, 9]);
