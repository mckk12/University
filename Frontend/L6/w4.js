function compareObjects(obj1, obj2) {
  if (typeof obj1 !== 'object' || typeof obj2 !== 'object') {
    return false;
  }
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);
  if (keys1.length !== keys2.length) {
    return false;
  }

  for (let key of keys1) {
    if (!keys2.includes(key) || obj1[key] !== obj2[key]) {
        if (typeof obj1[key] === 'object' && typeof obj2[key] === 'object') {
            if (!compareObjects(obj1[key], obj2[key])) {
                return false;
            }
        } else {
            return false;
        }
    }
  }

  return true;
}

const obj1 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
  };
  
  const obj2 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
  };
  
  const obj3 = {
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
    name: "Alice",
  };
  
  const obj4 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Not Wonderland",
      country: "Fantasy",
    },
  };
  
  const obj5 = {
    name: "Alice",
  };
  
  console.log("Should be True:", compareObjects(obj1, obj2));
  console.log("Should be True:", compareObjects(obj1, obj3));
  console.log("Should be False:", compareObjects(obj1, obj4));
  console.log("Should be True:", compareObjects(obj2, obj3));
  console.log("Should be False:", compareObjects(obj2, obj4));
  console.log("Should be False:", compareObjects(obj3, obj4));
  console.log("Should be False:", compareObjects(obj1, obj5));
  console.log("Should be False:", compareObjects(obj5, obj1));