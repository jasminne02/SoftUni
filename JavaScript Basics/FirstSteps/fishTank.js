function tank(input){
    let lenght = Number(input[0]);
    let width = Number(input[1]);
    let hight = Number(input[2]);
    let percent = Number(input[3]);
    let volume = lenght*width*hight;
    volume = volume/1000;
    volume = volume - volume * 0.01 * percent;
    console.log(volume);
}

tank([85,75,47,17]);
tank([105,77,89,18.5]);
