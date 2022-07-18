function solve(input){
    let array = input[0].split(" ").map(x => Number(x));

    for (let idx=1; idx<input.length; idx++){
        let command = String(input[idx]);
        
        if (command.includes("Add")){
            command = command.split(" ");
            number = Number(command[1]);
            array.push(number);
        } else if (command.includes("RemoveAt")){
            command = command.split(" ");
            number = Number(command[1]);
            array.splice(number, 1);
        } else if (command.includes("Remove")){
            command = command.split(" ");
            number = Number(command[1]);
            index = array.indexOf(number);
            array.splice(index, 1);
        } else if (command.includes("Insert")){
            command = command.split(" ");
            number = Number(command[1]);
            index = Number(command[2]);
            array.splice(index, 1, number);
        } 
    }

    return array.join(" ");
}

console.log(solve(['4 19 2 53 6 43',
'Add 3',
'Remove 2',
'RemoveAt 1',
'Insert 8 3']));
