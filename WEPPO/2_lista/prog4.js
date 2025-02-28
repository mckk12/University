const person = {
  name: 'Jan',
  age: 20,
};

var ClassFirst = function () {};
var ClassSecond = function () {};
var instance = new ClassFirst();

console.log(typeof person); // object
console.log(typeof person.name); // string

console.log(person instanceof Object); // true
console.log(person instanceof Array); // false


console.log(instance instanceof Object); // true
console.log(instance instanceof ClassFirst); // true
console.log(instance instanceof ClassSecond); //false