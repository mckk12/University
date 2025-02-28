function createGenerator(limit) {
    var _state = 0;
    return function() {         //funkcja generujaca
        return{
            next : function() {         //obiekt z wartosciami
                return {
                    value : _state,
                    done : _state++ >= limit
                }
            }
        }
    }
};


var foo = {
    [Symbol.iterator] : createGenerator(17)
};
for ( var f of foo )
    console.log(f);

var foo1 = {
    [Symbol.iterator] : createGenerator(13)
};
for ( var f of foo1 )
    console.log(f);

var foo2 = {
    [Symbol.iterator] : createGenerator(3)
};
for ( var f of foo2 )
    console.log(f);