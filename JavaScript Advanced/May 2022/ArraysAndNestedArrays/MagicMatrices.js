function solve(matrix){
    let number = undefined;
    for (let r = 0; r<matrix.length; r++){
        let sum = 0;
        for (let c = 0; c<matrix[r].length; c++){
            sum += matrix[r][c];
        }
        if (number == undefined){
            number = sum;
        } else if (number != sum){
            return false;
        }
    }
    
    let r = 0;
    for (let c = 0; c<matrix[r].length; c++){
        let sum = 0;
        for (let r = 0; r<matrix.length; r++){
            sum += matrix[r][c];
        } 
        if (number != sum){
            return false;
        }
    }

    return true;
}

console.log(solve([[4, 5, 6],
                   [6, 5, 4],
                   [5, 5, 5]]));

console.log(solve([[11, 32, 45], [21, 0, 1], [21, 1, 1]]));

console.log(solve([[1, 0, 0], [0, 0, 1], [0, 1, 0]]));
