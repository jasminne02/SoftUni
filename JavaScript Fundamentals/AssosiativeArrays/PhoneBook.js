function solve(input){
    let phoneBook = {};

    for (let info of input){
        let [name, number] = info.split(" ");
        phoneBook[name] = number;
    }

    for (let name in phoneBook){
        console.log(`${name} -> ${phoneBook[name]}`);
    }
}

solve(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344']);
