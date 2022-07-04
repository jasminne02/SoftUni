function equipment(input){
    let shoes = Number(input[0]) - Number([input[0]])*0.4;
    let outfit = shoes - shoes*0.2;
    let ball = outfit / 4;
    let accss = ball / 5;
    let total = Number(input[0])+shoes+outfit+ball+accss;
    console.log(total);
}

equipment([365]);
equipment([550]);
