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

(* ZAD 1 *)

(*

forall e. eval_rpn (to_rpn e) [] = eval e

*)

(* ZAD 2 *)

let rec from_rpn (r : rpn) (s : expr list) : expr =
  failwith "not implemented!"
  
(* ZAD 3 *)

(* porównaj zad 3. z listy 6. *)

let rec random_expr (max_depth : int) : expr =
  failwith "not implemented!"

let rec test (max_depth : int) (sample : int) : bool =
  failwith "not implemented!"

(* ZAD 4 *)

let rec test_ce (max_depth : int) (sample : int) : expr option =
  failwith "not implemented!"

(* ZAD 5 *)

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

end
