type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree
let t = Node ( Node ( Leaf , 2, Leaf ), 5, (Node (( Node ( Leaf , 6, Leaf)) , 8, ( Node ( Leaf , 9, Leaf )))))

let rec fold_tree f a t =
  match t with
  | Leaf -> a
  | Node (l, v, r) -> f (fold_tree f a l) v (fold_tree f a r)

(* let flatten t = fold_tree (fun l v r -> l @ [v] @ r) [] t *) (* original implementation *)
let build_list n f = 
  let rec it acc i = 
    if i = 0 then acc
    else it (f i :: acc) (i-1)
  in
  it [] n
;;

let left_tree_of_list xs =
  List.fold_left (fun t x -> Node (t, x, Leaf)) Leaf xs
  let test_tree = left_tree_of_list ( build_list 20000 Fun.id )
;;

let rec flat_append tree xs =
  match tree with
  | Leaf -> xs
  | Node (left, v, right) -> flat_append left (v :: flat_append right xs)
;;

let flatten t = flat_append t [];;

let rec print_int_list l = 
  match l with
  | [] -> print_string "\n"
  | h::t -> print_int h; print_string " "; print_int_list t
;;


print_int_list (flatten t)