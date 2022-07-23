function solve(input){
    let regex = /[A-Z]{1}[a-z]+\ [A-Z]{1}[a-z]+/g;
    let matches = input.match(regex);
    let result = [];
    
    for (let match of matches){
        if (result.includes(match)){
            continue;
        } else {
            result.push(match);
        }
    }

    return result.join(" ");
}

console.log(solve("Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan Ivanov"));
