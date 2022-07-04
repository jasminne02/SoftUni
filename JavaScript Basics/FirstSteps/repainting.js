function repating(input){
    let naylon = Number(input[0])*1.5;
    let paint = Number(input[1])*14.5;
    let litres = Number(input[2])*5;
    let hours = Number(input[3]);
    paint += paint * 0.1;
    naylon += 2 * 1.5;
    let total = naylon+paint+litres+hours+0.4;
    total += hours * 0.3 * total;
    console.log(total);
}

repating([10, 11, 4, 8])
repating([5, 10, 10, 1])
