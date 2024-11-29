type User = {
    name: string;
    age: number;
    occupation: string;
}

type Admin = {
    name: string;
    age: number;
    role: string;
}
export type Person = User | Admin;
    
export const persons: Person[] = [
    {
    name: 'Jan Kowalski',
    age: 17,
    occupation: 'Student'
    },
    {
    name: 'Tomasz Malinowski',
    age: 20,
    role: 'Administrator'
    }
];

function logPerson(person: Person) {
    let additionalInformation: string;
    if ('role' in person) {
        additionalInformation = person.role;
    } else {
        additionalInformation = person.occupation;
    }
    console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`);
}

//Person.role jest złą opcją, ponieważ typ Person może być zarówno typem User, jak i typem Admin. 
// Jednak tylko typ Admin ma pole role. Dlatego, jeśli person jest typu User, dostęp do pola role spowoduje błąd. 
// Aby uniknąć tego błędu, można użyć operatora typeof, aby sprawdzić, czy person jest typem Admin.

for (let person of persons ){
    logPerson(person);
}