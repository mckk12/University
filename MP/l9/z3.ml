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
  match r with
  | [] -> failwith "error!"
  | Push n :: r' -> Int n
  | RAdd :: r' ->
      let e2 = from_rpn r' in
      let e1 = from_rpn (List.tl r') in
      Add (e1, e2)
  | RMult :: r' ->
      let e2 = from_rpn r' in
      let e1 = from_rpn (List.tl r') in
      Mult (e1, e2)


let rec from_rpn (r : rpn) (s : expr list) : expr =
  match r, s with
  | [], [e] -> e
  | Push n :: r', _ -> from_rpn r' (Int n :: s)
  | RAdd :: r', e1 :: e2 :: s' -> from_rpn r' (Add (e2, e1) :: s')
  | RMult :: r', e1 :: e2 :: s' -> from_rpn r' (Mult (e2, e1) :: s')
  | _,_ -> failwith "error!"
  
let rec random_expr (max_depth : int) : expr =
  if max_depth = 0 then
    Int (Random.int 10)
  else
    match Random.int 3 with
    | 0 -> Add (random_expr (max_depth - 1), random_expr (max_depth - 1))
    | 1 -> Mult (random_expr (max_depth - 1), random_expr (max_depth - 1))
    | 2 -> Int (Random.int 10)
    | _ -> failwith "error!"

let rec test (max_depth : int) (sample : int) : bool =
  if sample = 0 then
    true
  else
    let e = random_expr max_depth in
    let e' = from_rpn (to_rpn e) [] in
    e = e' && test max_depth (sample - 1)