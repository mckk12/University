function isDivisibleByDigitAndSum(number) {
    const digits = String(number).split('').map(Number);
    var sumOfDigits = 0;
    for (const digit of digits){
        sumOfDigits+=digit;
    }
  
    for (const digit of digits) {
      if (digit === 0 || number % digit !== 0 || number % sumOfDigits !== 0) {
        return false;
      }
    }
  
    return true;
  }
  
const divisibleNumbers = [];
for (let i = 1; i <= 100000; i++) {
    if (isDivisibleByDigitAndSum(i)) {
        divisibleNumbers.push(i);
    }
}
console.log(divisibleNumbers);
