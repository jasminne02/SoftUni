function solve(object){
    for (let key of Object.keys(object)){
        console.log(`${key} -> ${object[key]}`);
    }
}

solve({name: "Sofia", area: 492, population: 1238438, country: "Bulgaria", pastCode: "1000"});
