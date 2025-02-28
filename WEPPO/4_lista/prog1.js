function getLastProto(o) {
    var p = o;
    do {
        o = p;
        p = Object.getPrototypeOf(o);
    } while (p);

    return o;
}

let obj1 = {};
let obj2 = Object.create(obj1);
let obj3 = new Date();
let obj4 = {
    name: "Jan"
};

Object.setPrototypeOf( obj1, obj4 );


let lastProto1 = getLastProto(obj1);
let lastProto2 = getLastProto(obj2);
let lastProto3 = getLastProto(obj3);
let lastProto4 = getLastProto(obj4);

console.log(lastProto1 === lastProto2); // true
console.log(lastProto1 === lastProto3); // true
console.log(lastProto1 === lastProto4); // true
