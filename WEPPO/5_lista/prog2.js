const stdin = process.stdin

console.log('Podaj imie: ')


stdin.addListener('data', text => {
  const name = text.toString().trim()
  console.log('Witaj ' + name)
  stdin.pause() // stop reading
})

