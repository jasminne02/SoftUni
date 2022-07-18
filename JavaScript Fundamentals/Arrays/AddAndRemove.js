function solve(commands){
    let array = [];
    let count = 1;

    for (let idx = 0; idx < commands.length; idx++){
        if (commands[idx] == "add"){
            array.push(count);
        } else if (commands[idx] == "remove"){
            array.pop();
        }

        count += 1;
    }

    console.log(array.join(" "));
}

solve(["add", "add", "add", "add"]);
console.log();
solve(["add", "add", "remove", "add", "add"]);
