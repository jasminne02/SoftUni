function sumVowels(input){
    let text = input[0];
    let sum = 0;
    for (let idx = 0; idx < text.length; idx++){
        switch (text[idx]){
            case "a": sum += 1; break;
            case "e": sum += 2; break;
            case "i": sum += 3; break;
            case "o": sum += 4; break;
            case "u": sum += 5; break;
        }
    }

    console.log(sum);
}

sumVowels(["beer"]);
sumVowels(["hello"]);
