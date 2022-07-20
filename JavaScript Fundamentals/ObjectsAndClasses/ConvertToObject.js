function solve(jsonFile){
    let object = JSON.parse(jsonFile);
    
    for (let [key, value] of Object.entries(object)){
        console.log(`${key}: ${value}`);
    }
}

solve('{"name": "George", "age": 40, "town": "Sofia"}');
