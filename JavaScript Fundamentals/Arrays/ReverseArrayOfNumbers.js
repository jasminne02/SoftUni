function reverse(number, array){
    let newArray = [];
    let finalArray = [];

    for (let i=0; i < number; i++){
        newArray[i] = array[i];
    }

    for (let idx=number-1; idx >= 0; idx--){
        finalArray.push(newArray[idx]);
    }

    console.log(finalArray.join(" "));
}

reverse(3, [10, 20, 30, 40, 50]);
