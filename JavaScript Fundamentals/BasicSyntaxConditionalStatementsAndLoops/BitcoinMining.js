function solve(input){
    let bitcoins = 0;
    let totalMoney = 0;
    let firstDayBought = 0;
    let boughtBitcoin = false;

    for (let day = 0; day < input.length; day++){
        let gold = Number(input[day]);
        if ((day+1) % 3 === 0){
            gold -= gold * 0.3;
        }

        totalMoney += gold * 67.51;
        
        if (totalMoney >= 11949.16){
            let count = parseInt(totalMoney / 11949.16);
            totalMoney -= 11949.16 * count;
            bitcoins += count;

            if (!boughtBitcoin){
                firstDayBought = day+1;
                boughtBitcoin = true;
            }
        }
    }

    console.log(`Bought bitcoins: ${bitcoins}`);
    if (bitcoins > 0){
        console.log(`Day of the first purchased bitcoin: ${firstDayBought}`);
    }
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`);
}


solve([100, 200, 300]);
solve([3124.15, 504.212, 2511.124]);
