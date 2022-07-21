function solve(input){
    let items = new Map();

    for (let info of input){
        let [item, quantity] = info.split(" ");
        
        if (items.has(item)){
            quantity += items.get(item);
            items.set(item, quantity);
        } else {
            items.set(item, quantity);
        }
    }

    for (let [item, quantity] of items){
        console.log(`${item} -> ${quantity}`);
    }
}

solve(['tomatoes 10',
'coffee 5',
'olives 100',
'coffee 40']);
