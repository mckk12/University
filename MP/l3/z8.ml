type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree

let t = Node ( Node ( Leaf , 2, Leaf ), 5, (Node (( Node ( Leaf , 6, Leaf)) , 8, ( Node ( Leaf , 9, Leaf )))))


let rec insert_bst x t =
  match t with
  | Leaf -> Node (Leaf, x, Leaf)
  | Node (l, v, r) -> 
      if x < v then Node (insert_bst x l, v, r)
      else Node (l, v, insert_bst x r)
;;

let rec flat_append tree xs =
  match tree with
  | Leaf -> xs
  | Node (left, v, right) -> flat_append left (v :: flat_append right xs)
;;

let flatten t = flat_append t [];;

let tree_sort xs = 
  let rec it xs t = 
    match xs with
    | [] -> t
    | x::xs' -> it xs' (insert_bst x t)
  in
  flatten(it xs Leaf)
;;

let rec print_int_list l = 
  match l with
  | [] -> print_string "\n"
  | h::t -> print_int h; print_string " "; print_int_list t
;;


print_int_list (tree_sort [5;7;3;4;8;9;2]);;