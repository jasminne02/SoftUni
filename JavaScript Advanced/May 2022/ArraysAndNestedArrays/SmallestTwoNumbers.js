function solve(array){
    let smallest1 = Math.min.apply(Math, array);
    array =  remove(array, smallest1);
    let smallest2 = Math.min.apply(Math, array);
    console.log(smallest1 + ' ' + smallest2);

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

solve([9, -89, 0, 67, 4]);
