const stdin = process.stdin


const randomNumber = Math.floor(Math.random() * 100)
console.log('Podaj liczbe: ')

stdin.addListener('data', text => {
  const num = text.toString().trim()
  
  if (num == randomNumber){
    stdin.pause() // stop reading
    console.log('to jest wlasnie ta liczba')
  }
  else if (num > randomNumber){
    console.log('moja liczba jest mniejsza')
  }
  else{
    console.log('moja liczba jest wieksza')
  }
})