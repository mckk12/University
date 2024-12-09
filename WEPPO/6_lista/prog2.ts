function memoize<T, U>(fn: (arg0: T) => U): (arg0: T) => U {
    const cache: { [key: string]: U } = {};
    return function (n: T): U {
        const key = JSON.stringify(n);
        if (key in cache) {
            return cache[key];
        } else {
            const result = fn(n);
            cache[key] = result;
            return result;
        }
    };
}

function fib(n: number): number {
    if (n <= 1) {
        return n;
    }

    return fib(n - 1) + fib(n - 2);
}

const memofib = memoize(fib);

console.time("fib");
console.log(memofib(40));
console.timeEnd("fib");

console.time("memfib");
console.log(memofib(40));
console.timeEnd("memfib");