var p = {
    name: 'jan'
}
var q = {
    surname: 'kowalski'
}
Object.setPrototypeOf( p, q );

console.log( p.name );
console.log( p.surname );
console.log('------------------');

function isOwnProperty(obj, prop) { // czy właściwość pochodzi bezpośrednio z obiektu
    return obj.hasOwnProperty(prop);
}


for (let prop in p) { // tylko właściwości z obiektu
    if (p.hasOwnProperty(prop)) {
        console.log(prop);
    }
}

console.log('------------------');
for (let prop in p) { // właściwości z obiektu i łańcucha prototypów
    console.log(prop);
}