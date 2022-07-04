function food(input){
    let chicken = Number(input[0])*10.35;
    let fish = Number(input[1])*12.40;
    let vegan = Number(input[2])*8.15;
    let total = chicken + fish + vegan;
    total += total*0.2;
    total += 2.50;
    console.log(total);
}

food([2, 4, 3]);
food([9, 2, 6]);
