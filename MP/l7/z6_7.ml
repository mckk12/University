type ident = string

type qbf =
  | Top (*true*)
  | Bot (*false*)
  | Var of ident
  | Forall of ident * qbf
  | Exists of ident * qbf
  | Not of qbf
  | Conj of qbf * qbf (*and*)
  | Disj of qbf * qbf  (*or*)


module Subst = struct

let rec subst (x : ident) (s : qbf) (f : qbf) : qbf =
  match f with
  | Top -> Top
  | Bot -> Bot
  | Var y -> if x = y then s else f
  | Forall (y, f') -> Forall (y, subst x s f')
  | Exists (y, f') -> Exists (y, subst x s f')
  | Not f' -> Not (subst x s f')
  | Conj (f1, f2) -> Conj (subst x s f1, subst x s f2)
  | Disj (f1, f2) -> Disj (subst x s f1, subst x s f2)
  
let rec eval (f : qbf) : bool =
  match f with
  | Top -> true
  | Bot -> false
  | Var x -> failwith ("free variable " ^ x)
  | Forall (x, f) -> eval (subst x Top f) && eval (subst x Bot f)
  | Exists (x, f) -> eval (subst x Top f) || eval (subst x Bot f)
  | Not f' -> not (eval f')
  | Conj (f1, f2) -> (eval f1) && (eval f2)
  | Disj (f1, f2) -> (eval f1) || (eval f2)

end

module Env = struct
module M = Map.Make(String)
type env = bool M.t
let rec eval_env (env : env) (f : qbf) : bool = 
    match f with
    | Top -> true
    | Bot -> false
    | Var x -> (match M.find_opt x env with
            | Some v -> v
            | None -> failwith ("free variable " ^ x))
    | Forall (x, f) -> eval_env (M.add x true env) f && eval_env (M.add x false env) f
    | Exists (x, f) -> eval_env (M.add x true env) f || eval_env (M.add x false env) f
    | Not f' -> not (eval_env env f')
    | Conj (f1, f2) -> (eval_env env f1) && (eval_env env f2)
    | Disj (f1, f2) -> (eval_env env f1) || (eval_env env f2)


end

module M = Map.Make(String)
let q = Forall ("x", Exists ("y", Exists ("z", Conj (Var "z", Disj (Var "y", Var "x")))))

let x = Env.eval_env M.empty q
let y = Subst.eval q
