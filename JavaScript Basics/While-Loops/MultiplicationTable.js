function multiplicationTable(){
    for (let f = 1; f <= 10; f++){
        for (let s = 1; s <= 10; s++){
            console.log(`${f} * ${s} = ${f*s}`);
        }
        console.log();
    }
}

multiplicationTable();
