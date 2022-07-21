function solve(input){
    let info = {};

    for (let infoString of input){
        let [weekday, name] = infoString.split(" ");
        
        if (weekday in info){
            console.log(`Conflict on ${weekday}!`);
        } else {
            info[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
        }
    }

    for (let [weekday, name] of Object.entries(info)){
        console.log(`${weekday} -> ${name}`);
    }
}

solve(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim']);
