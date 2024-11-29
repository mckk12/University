function fib() {
    var _state = 0;
        return{
            next : function() {   

                return {
                    value : _state,
                    done : _state++ >= limit
                }
            }
        }
}