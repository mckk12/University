let empty_set = [];;

let singleton a = [a];;

let rec in_set a s =
  match s with
  | [] -> false
  | h::t -> if h = a then true else in_set a t
;;

let rec union s1 s2 = 
  match s1 with
  | [] -> s2
  | h::t -> if in_set h s2 then union t s2 else h::(union t s2)
;;

let rec intersect s1 s2 =
  match s1 with
  | [] -> []
  | h::t -> if in_set h s2 then h::(intersect t s2) else intersect t s2
;;

(* 
let empty_set _ = false;;

let singleton a = fun x -> x = a;;

let in_set a s = s a;;

let union s t = fun x -> s x || t x;;

let intersect s t = fun x -> s x && t x;; *)



