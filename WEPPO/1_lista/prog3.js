function isPrime(num) {
    if (num < 2) {
      return false;
    }
  
    for (let i = 2; i < num; i++) {
      if (num % i == 0) {
        return false;
      }
    }
  
    return true;
  }

const primes = [];

for (let i = 2; i <= 100000; i++) {
    if (isPrime(i)) {
        primes.push(i);
    }
}

console.log(primes);
