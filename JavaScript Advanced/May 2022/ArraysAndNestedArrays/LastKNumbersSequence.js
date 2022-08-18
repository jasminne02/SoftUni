function solve(n, k){
    let sequence = [1];

    for (let i = 1; i < n; i++){
        let number = 0;
        let count = 0;
        let idx = i-1;
        while(count < k){
            if (idx < 0){
                break;
            }
            number += sequence[idx];
            idx--;
            count++;
        }
        sequence.push(number);
    }

    return sequence;
}

console.log(solve(5, 2));
console.log(solve(8, 3));
