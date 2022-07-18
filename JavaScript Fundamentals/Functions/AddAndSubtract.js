function addAndSubtract(num1, num2, num3){
    let sumed = sum(num1, num2);
    let result = subtract(sumed, num3);
    return result;

    function sum(num1, num2){
        return num1 + num2;
    }

    function subtract(num, num3){
        return num - num3;
    }
}

console.log(addAndSubtract(23, 6, 10));
