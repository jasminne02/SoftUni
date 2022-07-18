function solve(array){
    let step = Number(array[array.length - 1]);
    let result = "";

    for (let idx=0; idx<array.length; idx+=step){
        result += array[idx] + " ";
    }

    result = result.trim();

    console.log(result);
}

solve(['5', '20', '31', '4', '20', '2']);
