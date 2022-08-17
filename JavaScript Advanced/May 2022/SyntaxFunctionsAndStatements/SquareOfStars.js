function solve(count){
    for (n = 0; n < count; n++){
        let line = '';
        for (i = 0; i < count; i++){
            line += '* ';
        }
        console.log(line.trim());
    }
}

solve(3);
