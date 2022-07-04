function books(input){
    let pages = Number(input[0]);
    let readPerHour = Number(input[1]);
    let days = Number(input[2]);
    console.log((pages/readPerHour)/days);
}

books([212, 20, 2]);
books([432, 15, 4]);
