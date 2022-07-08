function lucnBreak(input){
    let seriesName = input[0];
    let seriesDuration = Number(input[1]);
    let lunchDuratoin = Number(input[2]);
    let totalTime = lunchDuratoin;

    totalTime -= lunchDuratoin / 8;
    totalTime -= lunchDuratoin / 4;
    totalTime -= seriesDuration;

    if (totalTime >= 0){
        console.log(`You have enough time to watch ${seriesName} and left with ${totalTime} minutes free time.`);
    } else {
        console.log(`You don't have enough time to watch ${seriesName}, you need ${Math.abs(totalTime)} more minutes.`);
    }
}


lucnBreak(["Game of Thrones", "60", "96"]);
