function petshop(input){
    let dogFood = Number(input[0]) * 2.5;
    let catFood = Number(input[1]) * 4;
    let finalSum = dogFood + catFood;
    console.log(`${finalSum} lv.`);
}

petshop(["5", "4"]);
petshop(["13", "9"]);
