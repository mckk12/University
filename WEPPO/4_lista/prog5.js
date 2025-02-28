
function Foo() {
  function Qux() {
    console.log('private');
  }

  this.Bar = function() {
    console.log('public');
    Qux();
    // return function() {
    //   console.log('private');
    // }();
  }
}


const foo1 = new Foo();
foo1.Bar(); 
console.log('------------------');
const foo2 = new Foo();
foo2.Bar(); 
//foo2.Qux(); // TypeError: foo2.Qux is not a function
//Foo().Qux()