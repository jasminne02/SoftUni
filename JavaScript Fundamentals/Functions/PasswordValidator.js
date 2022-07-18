function validatePassword(password){
    let validLength = true;
    let digitsCount = 0;
    let validChars = true;

    if (String(password).length < 6 || String(password).length > 10){
        validLength = false;
    }
    
    for(let i=0; i<String(password).length; i++){
        let value = password[i].charCodeAt();
        if (value >= 48 && value <= 57){
            // checks digits
            digitsCount++;
        } else if (value >= 65 && value <= 90) {
            // checks capital letters
            continue;
        } else if (value >= 97 && value <= 122){
            // checks letters
            continue;
        } else {
            validChars = false;
        }
    }

    if (!validLength){
        console.log("Password must be between 6 and 10 characters");
    }
    if (!validChars){
        console.log("Password must consist only of letters and digits");
    }
    if (digitsCount < 2){
        console.log("Password must have at least 2 digits");
    }
    if (validLength && validChars && digitsCount > 2){
        console.log("Password is valid");
    }
}

validatePassword("logIn");
console.log();
//validatePassword("MyPass123");
