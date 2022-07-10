function solve(input){
    let username = String(input[0]);
    let usernameSplit = username.split("");
    let passwordSplit = usernameSplit.reverse();
    let password = passwordSplit.join("");
    let idx = 1;
    
    while (true){
        if (input[idx] !== password){
            console.log("Incorrect password. Try again.");
        } else {
            console.log(`User ${username} logged in.`);
            break;
        }
        idx++;
    }
}


solve(["Acer", "login", "go", "let me in", "recA"]);
