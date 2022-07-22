function solve(input, word){
    let text = String(input);
    let result = text.replace(word, '*'.repeat(word.length));;
    while (result.includes(word)){
        let result = text.replace(word, '*'.repeat(word.length));
    }
    return result;
}

console.log(solve("A small sentence with some words", "small"));
