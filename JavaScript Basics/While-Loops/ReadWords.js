function read(input){
    let idx = 0;

    while (input[idx] != "Stop"){
        console.log(input[idx]);
        idx++;
    }
}


read(["Nakov", "SoftUni", "Sofia", "Plovdiv", "Stop", "Bye"]);
