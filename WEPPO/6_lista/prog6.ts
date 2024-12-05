type User = {
    type: 'user';
    name: string;
    age: number;
    occupation: string;
}

type Admin = {
    type: 'admin';
    name: string;
    age: number;
    role: string;
}
export type Person = User | Admin;
    
export const persons: Person[] = [
    {
        type: 'user',
        name: 'Jan Kowalski',
        age: 17,
        occupation: 'Student'
    },
    {
        type: 'admin',
        name: 'Tomasz Malinowski',
        age: 20,
        role: 'Administrator'
    },
    {
        type: 'user',
        name: 'Mariusz Nowak',
        age: 23,
        occupation: 'Student'
    },
    
];

export function isAdmin(person: Person) {
    return person.type === 'admin';
}

export function isUser(person: Person) {
    return person.type === 'user';
}

export function logPerson(person: Person) {
    let additionalInformation: string = '';
    if (isAdmin(person)) {
        additionalInformation = (person as Admin).role;
    }
    if (isUser(person)) {
        additionalInformation = (person as User).occupation;
    }
    console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`);
}

for (let person of persons ){
    logPerson(person);
}