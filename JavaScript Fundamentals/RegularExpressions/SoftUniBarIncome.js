function solve(input){
    let text = input.join(" ");
    let regex = /\%(?<name>[A-Z][a-z]+)\%\<(?<product>[A-Za-z]+)\>\|(?<count>\d+)\|(?<price>\d+[.]\d+)\$/g;
    let valid;

    while ((valid = regex.exec(text)) !== null){
        let name = valid.groups.name;
        let product = valid.groups.product;
        let count = valid.groups.count;
        let price = valid.groups.price;

        console.log(`${name}: ${product} - ${price*count}`);
    }

}

solve(['%George%<Croissant>|2|10.3$',
'%Peter%<Gum>|1|1.3$',
'%Maria%<Cola>|1|2.4$',
'end of shift']);
