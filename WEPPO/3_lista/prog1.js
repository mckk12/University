function memoize(fn) {
    var cache = {};
    return function(n) {
        if ( n in cache ) {
            console.log("n: " + n);
            return cache[n];
        } else {
            var result = fn(n);
            cache[n] = result;
            return result;
        }
    }
}

function fib(n) {
    if ( n < 2 ) {
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

var fib = memoize(fib);

console.time("fib");
console.log(fib(40));
console.timeEnd("fib");

console.time("memfib");
console.log(fib(30));
console.timeEnd("memfib");

