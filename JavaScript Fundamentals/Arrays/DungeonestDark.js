function solve(array){
    let rooms = String(array[0]).split("|");
    let health = 100;
    let coins = 0;
    let bestRoom = 0;

    for (let room of rooms){
        room = room.split(" ");
        let item = room[0];
        let monsterNumber = Number(room[1]);
        bestRoom += 1;

        if (item == "potion"){
            let healingNumber = monsterNumber;

            if(health + monsterNumber <= 100){
                health += monsterNumber;
            } else {
                healingNumber = 100 - health;
                health = 100;
            }
            
            console.log(`You healed for ${healingNumber} hp.`);
            console.log(`Current health: ${health} hp.`);
        } else if (item == "chest"){
            coins += monsterNumber;
            console.log(`You found ${monsterNumber} coins.`);
        } else {
            health -= monsterNumber;

            if (health > 0) {
                console.log(`You slayed ${item}.`);
            } else{
                console.log(`You died! Killed by ${item}.`);
                console.log(`Best room: ${bestRoom}`);
                break;
            }
        }
    }

    if (bestRoom == rooms.length){
        console.log(`You've made it!`);
        console.log(`Coins: ${coins}`);
        console.log(`Health: ${health}`);
    }
}

solve(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);

