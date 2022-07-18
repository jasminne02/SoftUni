function matrix(number){
    let matrix = [];

    for (let row=0; row<number; row++){
        let line = [];
        for (let col=0; col<number; col++){
            line.push(number);
        }
        matrix.push(line);
    }

    for (let row=0; row<number; row++){
        let line = "";
        for (let col=0; col<number; col++){
            line += String(matrix[row][col]) + " ";
        }
        line.trim();
        console.log(line);
    }

}

matrix(3);
