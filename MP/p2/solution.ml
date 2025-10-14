(* abstract syntax tree *)

type bop = Mult | Div | Add | Sub | Eq | Lt | Gt | Leq | Geq | Neq

type ident = string

type expr =
  | Int of int
  | Bool of bool
  | Binop of bop * expr * expr
  | If of expr * expr * expr
  | Var of ident
  | Let of ident * expr * expr

module H = Map.Make(String)

(* konwersja wyrazenia do stringa *)
let convert (e : expr) : expr =
  let rec aux e env = 
    match e with
    | Int _ | Bool _ -> e
    | Var x -> (match H.find_opt x env with
                  | Some l -> Var (string_of_int !l)
                  | None   -> e)
    | Binop (bop, e1, e2) ->
        Binop (bop, aux e1 env, aux e2 env)
    | If (e1, e2, e3) ->
        If (aux e1 env, aux e2 env, aux e3 env)
    | Let (x, e1, e2) -> let env' = H.add x (ref 0) env in
        Let ("_", aux e1 env, aux e2 env')
  in
  aux e H.empty

(* sprawdzanie czy w listach wystepuja 2 expr alpha rownowazne *)
let check_alpha (l1 : expr list) (l2 : expr list) : expr option =
  let rec find_alpha_equiv_expr l1 l2 =
    match l1 with
    | [] -> None
    | e1 :: rest1 ->
        match List.find_opt (fun e2 -> convert e1 = convert e2) l2 with
        | Some _ -> Some e1
        | None -> find_alpha_equiv_expr rest1 l2
  in
  find_alpha_equiv_expr l1 l2

(* postawienie nowej zmiennej pod wyrazenia alpha rownowazne *)
let rec substitute (e:expr) (x : ident) (c : expr) : expr =
  match e with
  | Int _ | Bool _ | Var _ -> e
  | Binop (bop, e1, e2) -> if Binop (bop, e1, e2) = c then Var x else Binop (bop, substitute e1 x c, substitute e2 x c)
  | If (e1, e2, e3) -> if If (e1, e2, e3) = c then Var x else If (substitute e1 x c, substitute e2 x c, substitute e3 x c)
  | Let (y, e1, e2) -> if Let (y, e1, e2) = c then Var x else Let (y, substitute e1 x c, if y = x then e2 else substitute e2 x c)

(* usuniecie z listy exprow tych, ktore zawieraja ident *)
let clear_ident (el : expr list) (x : ident) : expr list =
  let rec aux el x acc =
    match el with
    | [] -> acc
    | e :: rest -> if let rec help e x = match e with 
            | Var y -> if y = x then true else false
            | Int _ | Bool _ -> false
            | Binop (_, e1, e2) -> (help e1 x) || (help e2 x)
            | If (e1, e2, e3) -> (help e1 x) || (help e2 x) || (help e3 x)
            | Let (y, e1, e2) -> (help e1 x) || (if y=x then false else help e2 x)
            in help e x
            then aux rest x acc else aux rest x (e :: acc)
  in aux el x []


let cse (e : expr) : expr option =
  let rec aux (e : expr) (env : expr list) : (expr option * expr list) =
    match e with
    | Int _ | Bool _ | Var _ -> None, []
    | Binop (bop, e1, e2) -> 
      let e1', env1 = aux e1 env in
      let e2', env2 = aux e2 env in
      (match e1', e2' with
      | Some e1'', Some e2'' -> Some (Binop (bop, e1'', e2'')), env1 @ env2
      | Some e1'', _ -> Some (Binop (bop, e1'', e2)), env1 @ env2
      | _, Some e2'' -> Some (Binop (bop, e1, e2'')), env1 @ env2
      | None, None -> match check_alpha env1 env2 with
                      | None -> None, (Binop (bop, e1, e2))::(env1 @ env2) 
                      | Some c -> Some (Let ("v", c, substitute (Binop (bop, e1, e2)) "v" c)), env1 @ env2)
    | If (e1, e2, e3) -> 
      let e1', env1 = aux e1 env in
      let e2', env2 = aux e2 env in
      let e3', env3 = aux e3 env in
      (match e1', e2', e3' with
      | Some e1'', Some e2'', Some e3'' -> Some (If (e1'', e2'', e3'')), env1 @ env2 @ env3
      | Some e1'', Some e2'', _ -> Some (If (e1'', e2'', e3)), env1 @ env2 @ env3
      | Some e1'', _, Some e3'' -> Some (If (e1'', e2, e3'')), env1 @ env2 @ env3
      | _, Some e2'', Some e3'' -> Some (If (e1, e2'', e3'')), env1 @ env2 @ env3
      | Some e1'', _, _ -> Some (If (e1'', e2, e3)), env1 @ env2 @ env3
      | _, Some e2'', _ -> Some (If (e1, e2'', e3)), env1 @ env2 @ env3
      | _, _, Some e3'' -> Some (If (e1, e2, e3'')), env1 @ env2 @ env3
      | None, None, None -> match check_alpha env1 env2 with
                            | None -> (match check_alpha env2 env3 with
                                      | None -> (match check_alpha env1 env3 with
                                                | None -> None, (If (e1, e2, e3))::env1 @ env2 @ env3
                                                | Some c -> Some (Let ("v", c, substitute (If (e1, e2, e3)) "v" c)), env1 @ env2 @ env3)
                                      | Some c -> Some (Let ("v", c, substitute (If (e1, e2, e3)) "v" c)), env1 @ env2 @ env3)
                            | Some c -> Some (Let ("v", c, substitute (If (e1, e2, e3)) "v" c)), env1 @ env2 @ env3)

    | Let (x, e1, e2) -> 
      let e1', env1 = aux e1 env in
      let e2', env2 = aux e2 env in
      (match e1', e2' with
      | Some e1'', Some e2'' -> Some (Let (x, e1'', e2'')), env1 @ env2
      | Some e1'', _ -> Some (Let (x, e1'', e2)), env1 @ env2
      | _, Some e2'' -> Some (Let (x, e1, e2'')), env1 @ env2
      | None, None -> 
        let env1' = clear_ident env1 x in
        let env2' = clear_ident env2 x in
        match check_alpha env1' env2' with
                      | None -> None, (Let (x, e1, e2))::env1' @ env2'
                      | Some c -> Some (Let ("v", c, substitute (Let (x, e1, e2)) "v" c)), env1' @ env2')
  in
  let e', _ = aux e [] in 
  e'


(* ;
cse(If(Var("x"), Binop(Add, Binop(Mult, Var("z"), Int(10)), Int(0)), Binop(Mult, Var("z"), Int(10))))
     Some Let(v, Binop(Mult, z, 10), If(Var("x"), Binop(Add,  Var("v"), Var("v"), Int(10)) *)
(* check_ae [Binop(Mult, Var("z"), Int(10)); Binop(Add, Binop(Mult, Var("z"), Int(10)), Int(0))] [Binop(Mult, Var("z"), Int(10))] *)
(* alpha_equiv (Binop(Mult, Var("z"), Int(10))) (Binop(Mult, Var("z"), Int(10))) *)
(* convert (Let ("x", Binop (Add, Binop (Mult, Var "z", Int 10), Binop (Mult, Var "z", Int 10)), Int 0)); *)