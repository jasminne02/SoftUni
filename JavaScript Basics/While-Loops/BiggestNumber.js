function findBiggestNumber(input){
    let maxNum = Number.MIN_SAFE_INTEGER;
    let idx = 0;
    while(input[idx] != "Stop"){
        if (maxNum < Number(input[idx])){
            maxNum = Number(input[idx]);
        }
        idx++;
    }
    console.log(maxNum);
}


findBiggestNumber(["100", "99", "23", "345", "54", "Stop"]);
findBiggestNumber(["34", "45", "345", "323", "654", "43", "Stop"]);
