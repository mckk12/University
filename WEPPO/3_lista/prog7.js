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


function* take(it, top) {
    for(let i = 0;i<top;i++){
        yield it.next().value;
    }
}
    // zwróć dokładnie 10 wartości z potencjalnie
    // "nieskończonego" iteratora/generatora
for (let num of take( fib(), 10 ) ) {
    console.log(num);
}