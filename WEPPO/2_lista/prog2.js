const obiekt = {
    name: 'nazwaobiektu',
    liczba: 2,
    "2.09.2003": "data",
    5: "pięć"
};
const key = "owoc";
obiekt[key] = "jabłko";

const tablica = [10, 20, 30]; //dodanie wl pod kluczem zmienia tablice w obiekt

console.log(obiekt.name); //identyfikator
console.log(obiekt['2.09.2003']);      //wyrażenie


const key1 = { toString: () => "name" };
console.log(obiekt[key1]);

console.log(obiekt[5]);  
console.log(obiekt['5']);
console.log(obiekt['owoc']);            

console.log(tablica['2']); //identyfikator



tablica["property"] = "Hello";
console.log(tablica.length); // Wynik: 3
console.log(tablica.property);

