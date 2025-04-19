function capitalize (str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
};

function capitalizeSentence (str) {
  return str.split(' ').map(capitalize).join(' ');
}

console.log("Task 2:");
console.log(capitalizeSentence("alice"));
console.log(capitalizeSentence("alice in wonderland"));