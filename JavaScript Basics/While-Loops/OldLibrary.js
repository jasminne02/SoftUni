function library(input){
    let favBook = input[0];
    let idx = 1;
    let found = false;

    while(input[idx] != "No More Books"){
        if (input[idx] == favBook){
            found = true;
            break;
        }
        idx++;
    }

    if (found){
        console.log(`You checked ${idx-1} books and found it.`);
    } else {
        console.log(`The book you search is not here!\nYou checked ${idx-1} books.`);
    }
}


library(["Troy", "Stronger", "Life Style", "Troy"]);
library(["The Spot", "Game of Thrones", "Harry Petter", "Torronto", "Spotify", "No More Books"]);
library(["Bourne", "True Story", "Forever", "The girl", "Spaceship", "Strongest", "Profit", "Tripple", "Stella", "The matrix", "Bourne"]);
