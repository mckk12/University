type expr =
  | Int of int
  | Add of expr * expr
  | Mult of expr * expr

let rec eval (e : expr) : int =
  match e with
  | Int n -> n
  | Add (e1, e2) -> eval e1 + eval e2
  | Mult (e1, e2) -> eval e1 * eval e2

type rpn_cmd =
  | Push of int
  | RAdd
  | RMult

type rpn = rpn_cmd list

let rec to_rpn (e : expr) : rpn =
  match e with
  | Int n -> [Push n]
  | Add (e1, e2) -> to_rpn e1 @ to_rpn e2 @ [RAdd]
  | Mult (e1, e2) -> to_rpn e1 @ to_rpn e2 @ [RMult]

let rec eval_rpn (r : rpn) (s : int list) : int =
  match r, s with
  | [], [n] -> n
  | Push n :: r', _ -> eval_rpn r' (n :: s)
  | RAdd :: r', n1 :: n2 :: s' -> eval_rpn r' (n2 + n1 :: s')
  | RMult :: r', n1 :: n2 :: s' -> eval_rpn r' (n2 * n1 :: s')
  | _,_ -> failwith "error!"

let rec from_rpn (r : rpn) : expr =
  let rec aux (r : rpn) (s : expr list) : expr =
    match r, s with
    | [], [e] -> e
    | Push n :: r', _ -> aux r' (Int n :: s)
    | RAdd :: r', e1 :: e2 :: s' -> aux r' (Add (e2, e1) :: s')
    | RMult :: r', e1 :: e2 :: s' -> aux r' (Mult (e2, e1) :: s')
    | _,_ -> failwith "error!"
  in
  aux r []

  