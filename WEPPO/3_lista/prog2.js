function forEach(a, f) {
    for (let i = 0; i < a.length; i++) {
        f(a[i]);
    }
}

function map(a, f) {
    const result = [];
    for (let i = 0; i < a.length; i++) {
        result.push(f(a[i]));
    }
    return result;
}

function filter(a, f) {
    const result = [];
    for (let i = 0; i < a.length; i++) {
        if (f(a[i])) {
            result.push(a[i]);
        }
    }
    return result;
}

const a = [1, 2, 3, 4];
forEach(a, (item) => console.log(item));
// [1,2,3,4]
filter(a, (item) => item < 3);
// [1,2]
map(a, (item) => item * 2);
// [2,4,6,8]
