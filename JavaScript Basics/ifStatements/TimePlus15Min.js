function time(input){
    let hour = Number(input[0]);
    let min = Number(input[1]);
    min += 15;

    if (min >= 60){
        hour += 1;
        min -= 60;
    }
    if (hour >= 24){
        hour -= 24;
    }

    if (min < 10){
        min = 0 + String(min);
    }

    console.log(`${hour}:${min}`);
}


time(["1", "46"]);
time(["0", "01"]);
