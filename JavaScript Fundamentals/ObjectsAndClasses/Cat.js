class Cat{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    
    speak(){
        console.log(`${this.name}, age ${this.age} says Meow`);
    }
}

function solve(input){
    for (let info of input){
        info = info.split(" ");
        let name = info[0];
        let age = Number(info[1]);

        let cat = new Cat(name, age);
        cat.speak();
    }
}

solve(['Mellow 2', 'Tom 5']);
