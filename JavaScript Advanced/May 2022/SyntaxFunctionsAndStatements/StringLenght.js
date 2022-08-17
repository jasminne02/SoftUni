function Function(string1, string2, string3){
    let textLenght = String(string1).length + String(string2).length + String(string3).length;
    let avrg = Math.floor(textLenght / 3)
    console.log(textLenght);
    console.log(avrg);
}

Function('Hello', 'there', 'Cat')
