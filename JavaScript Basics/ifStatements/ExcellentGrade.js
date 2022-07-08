function grade(input){
    let grade = Number(input[0]);
    if (grade >= 5.50){
        console.log("Excellent!");
    }
}


grade(["6"]);
grade(["5"]);
grade(["5.50"]);
grade(["5.49"]);
