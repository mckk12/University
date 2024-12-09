function memoize(fn) {
    var cache = {};
    return function(n) {
        if ( n in cache ) {
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

var memofib = memoize(fib);

console.time("fib");
console.log(memofib(40));
console.timeEnd("fib");

console.time("memfib");
console.log(memofib(40));
console.timeEnd("memfib");
