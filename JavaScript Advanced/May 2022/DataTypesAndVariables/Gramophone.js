function solve(band, album, song){
    let songDuration = (String(album).length * String(band).length) * String(song).length / 2;
    let rotations = Math.ceil(songDuration / 2.5);
    console.log(`The plate was rotated ${rotations} times.`)
}


solve("Black Sabbath", "Paranoid", "War Pigs");
