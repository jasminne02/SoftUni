function solve(letter){
    let result = String(letter).charAt(0) === String(letter).charAt(0).toLowerCase();
    console.log(result? "lower-case" : "upper-case");
}


solve('F');
solve("f");
