function charactersBetween(char1, char2){
    let result = "";
    let start = 0;
    let end = 0;

    if (char1.charCodeAt() < char2.charCodeAt()){
        start = char1.charCodeAt();
        end = char2.charCodeAt();
    } else {
        start = char2.charCodeAt();
        end = char1.charCodeAt();
    }

    for (let i=start+1; i<end; i++){
        result += String.fromCharCode(i) + " ";
    }

    return result.trim();
}

console.log(charactersBetween('a', 'd') + "\n");
console.log(charactersBetween('#', ':'));
