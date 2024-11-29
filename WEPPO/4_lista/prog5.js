
function Foo() {
  function Qux() {
    console.log('This is a private function');
  }

  this.Bar = function() {
    console.log('This is a public method');
    Qux(); 
  }
}


const foo1 = new Foo();
foo1.Bar(); 

const foo2 = new Foo();
foo2.Bar(); 
