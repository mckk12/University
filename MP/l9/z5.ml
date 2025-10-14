type bop = Mult | Div | Add | Sub | Eq | Lt | Gt | Leq | Geq | Neq

module T = struct

type cmd =
  | PushInt of int
  | PushBool of bool
  | Prim of bop
  | Jmp of string
  | JmpFalse of string
  | Grab
  | Access of int
  | EndLet
  | PushClo of string
  | Call of string
  | Return
  | Lbl of string

let flatten (c: cmd list) : cmd list =
  let rec aux acc = function
    | [] -> List.rev acc
    | Lbl _ :: t -> aux t acc
    | h :: t -> aux t (h :: acc)
  in
  aux [] c

end