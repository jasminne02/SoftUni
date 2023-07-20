function test(){
    let num = '4';
    if (4 == num){
        console.log('== - compares value not type')
    } else {
        console.log('== - compares value and type')
    }

    if(4 === num){
        console.log('=== - does not compare value')
    } else{
        console.log('=== - compares value and type')
    }
}

test();

