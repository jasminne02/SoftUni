function solve(word){
    let wordString = String(word).split("");
    let reversedWordSplit = wordString.reverse();
    let reversedWord = reversedWordSplit.join("");
    console.log(reversedWord);
}

solve("Hello");
