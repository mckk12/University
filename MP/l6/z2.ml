(* S -> ε
S -> a
S -> b
S -> aSa
S -> bSb *)

type 'a symbol =
    | E
    | T of string
    | N of 'a
  
  type 'a grammar = ('a * ('a symbol list) list) list


let palindrom : char grammar = 
  [('S', [ [E]; [T "a"]; [T "b"]; [T "a"; N 'S'; T "a"]; [T "b"; N 'S'; T "b"] ])];