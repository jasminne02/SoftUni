function solve(commands){
    let numbers = [];
    let n = 1;
    for (let command of commands){
        if ( command == 'add'){
            numbers.push(n);
        } else if (command == 'remove'){
            numbers.pop();
        }
        n++;
    }

    if (numbers.length == 0){
        numbers = 'Empty';
    }

    return numbers;
}

console.log(solve(['add', 'add', 'remove', 'add', 'add']))
