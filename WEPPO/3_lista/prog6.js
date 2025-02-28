function fib() {
    var pre = 0, cur = 1;
    return {
        next : function() {
            var temp = pre;
            [pre, cur] = [cur, pre + cur];            
            return {
                value : temp,
                done : false
            }
        }
    }
}

function *fib1() {
    var pre = 0, cur = 1;

    while(true){
        yield pre;
        [pre, cur] = [cur, pre + cur];
          
    }
}

var _it = fib();

for ( var _result; _result = _it.next(), _result.value<30; ) {
    console.log( _result.value );
}


var _it1 = fib1();

for ( var _result1; _result1 = _it1.next(), _result1.value<30; ) {
    console.log( _result1.value );
}


// for ( var i of fib1() ) { //tylko ten przypadek
//     console.log( i );
// }