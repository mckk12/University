const obiekt = {
    message: 'hello',
    method: function() {
        console.log(this.message);
    },
    get getter() {
        return this.message;
    },
    set setter(value) {
        this.message = value;
    }
};
obiekt.newMsg = 'world';
obiekt.newMethod = function() {
    console.log(this.newMsg);
};

Object.defineProperty(obiekt, 'newGetterSetter', {
    get: function() {
      return this.newMsg;
    },
    set: function(value) {
      this.newMsg = value;
    }
});

const msg = obiekt.getter;
console.log(msg);
obiekt.setter = 'hello!';
obiekt.method();

obiekt.newMethod();

obiekt.newGetterSetter = 'world!';
obiekt.newMethod();

