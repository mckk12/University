function Tree(val, left, right) {
    this.left = left;
    this.right = right;
    this.val = val;
    
}

Tree.prototype[Symbol.iterator] = function*() {
    var queue = [this];
    while (queue.length > 0){
        if ( queue[0].left ) queue.push(queue[0].left);
        if ( queue[0].right ) queue.push(queue[0].right);
        if (queue[0]) yield queue[0].val;
        queue.splice(0, 1);
    }
}


var root = new Tree( 1,
new Tree( 2, new Tree( 3 ) ), new Tree( 4 ));


for ( var e of root ) {
    console.log( e );
}

// jest 1 2 3 4
// chcemy 1 2 4 3
