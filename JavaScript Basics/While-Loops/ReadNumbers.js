function read(input){
    let sum = 0;
    let idx = 1;

    while (sum < Number(input[0])){
        sum += Number(input[idx]);
        idx++;
    }

    console.log(sum);
}

read(["100", "10", "20", "30", "40"]);
