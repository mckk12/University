function filter<T>( a: T[], f: (t: T) => boolean ): T[] {
    const result: T[] = [];
    for (const item of a) {
        if (f(item)) {
            result.push(item);
        }
    }
    return result;
}

function map<T, U>( a: T[], f: (t: T) => U ): U[] {
    const result: U[] = [];
    for (const item of a) {
        result.push(f(item));
    }
    return result;
}

function forEach<T>( a: T[], f: (t: T) => void ): void {
    for (const item of a) {
        f(item);
    }
}

let a = [1, 2, 3, 4, 5];
let b = filter(a, (x) => x % 2 === 0);
let c = map(a, (x) => x * x);

forEach(a, (x) => console.log(x));
forEach(b, (x) => console.log(x));
forEach(c, (x) => console.log(x));