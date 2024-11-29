function fibIter(n) {
    let prev = 0;
    let curr = 1;
  
    for (let i = 1; i <= n; i++) {
      const temp = curr;
      curr += prev;
      prev = temp;
    }
  
    return curr;
  }
  
function fibRec(n) {
    if (n <= 1) {
        return n;
    }

    return fibRec(n - 1) + fibRec(n - 2);
}

function measureExecutionTime(func, n) {
    console.time(`n = ${n}`);
    func(n);
    console.timeEnd(`n = ${n}`);
}

console.log('Times for Iteration:');
for(let i = 10; i<100;i++){
    measureExecutionTime(fibIter, i)
}

console.log('\nTimes for recursion:');
for(let i = 10; i<40;i++){
    measureExecutionTime(fibRec, i)
}