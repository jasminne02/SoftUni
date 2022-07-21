function solve(input){
    let firstLine = input.shift();
    let tracker = {};

    for (let word of firstLine.split(" ")){
        tracker[word] = 0;
    }

    for (let word of input){
        if (word in tracker){
            tracker[word] += 1;
        }
    }

    for (let [word, value] of Object.entries(tracker)){
        console.log(`${word} - ${value}`);
    }
}

solve([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have',
    'to', 'count', 'the', 'occurrences', 'of',
    'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task'
    ]);
