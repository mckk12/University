console.log("Task 3:");
const ids = [];

const generateId = () => {
  let id = 0;

  do {
    id++;
  } while (ids.includes(id));

  ids.push(id);
  return id;
};

const solIds =  new Set();
const solGenerateId = () => {
  let id = 0;

  do {
    id++;
  } while (solIds.has(id));

  solIds.add(id);
  return id;
};

console.time("generateId");
for (let i = 0; i < 3000; i++) {
  generateId();
}
console.timeEnd("generateId");
console.time("solGenerateId");
for (let i = 0; i < 3000; i++) {
  solGenerateId();
}
console.timeEnd("solGenerateId");
