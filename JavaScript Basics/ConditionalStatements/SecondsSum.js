function secondsSum(input){
    let first = Number(input[0]);
    let second = Number(input[1]);
    let third = Number(input[2]);
    let sum = first + second + third;
    let minutes = Math.floor(sum / 60);
    let seconds = sum % 60;
    if (seconds < 10){
        seconds = "0" + String(seconds);
    }
    console.log(`${minutes}:${seconds}`);
}


secondsSum(["35", "45", "44"]);
secondsSum(["22", "7", "34"]);
