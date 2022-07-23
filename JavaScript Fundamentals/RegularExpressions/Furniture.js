function solve(input){
    let text = input.join(" ");
    let regex = /\>\>(?<furniture>[A-Z]{1}[A-Za-z]+)\<\<(?<price>\d+([.]\d+)*)\!(?<quantity>\d+)/g;
    let boughtFurniture = [];
    let totalSpentMoney = 0;
    let valid;

    while ((valid = regex.exec(text)) !== null){
        let furniture = valid.groups.furniture;
        let price = valid.groups.price;
        let quantity = valid.groups.quantity;

        boughtFurniture.push(furniture);
        totalSpentMoney += price * quantity;
    }

    console.log("Bought furniture:");
    for (let furniture of boughtFurniture){
        console.log(furniture);
    }

    console.log(`Total money spend: ${totalSpentMoney}`);
}

solve(['>>Sofa<<312.23!3',
'>>TV<<300!5',
'>Invalid<<!5',
'Purchase']);
