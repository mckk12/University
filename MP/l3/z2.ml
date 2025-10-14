let compose f g a = f (g a)

let square a = a * a

let inc b = b + 1


let x = compose square inc 5;;
let y = compose inc square 5;;


print_int(x);;
print_newline();;
print_int(y);;
print_newline();;
