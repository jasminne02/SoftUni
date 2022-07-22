function solve(input){
    let text = String(input);
    let firstIdx = 0;
    let midIdx = Math.floor(text.length / 2);
    let lastIdx = text.length - 1;

    let firstPart = text.substring(firstIdx, midIdx);
    let secondPart = text.substring(midIdx, lastIdx);

    let x1 = "";
    let x2 = "";

    for (let idx = firstPart.length-1; idx >= 0; idx--){
        x1 += firstPart[idx];
    }

    console.log(x1);
    console.log(x2);

}


solve('SplitMeIfYouCanHaHaYouCantOrYouCan');
