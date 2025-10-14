type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree
let rec fold_tree f a t =
  match t with
  | Leaf -> a
  | Node (l, v, r) -> f (fold_tree f a l) v (fold_tree f a r)
;;

let te = Node ( Node ( Leaf , 2, Leaf ), 5, (Node (( Node ( Leaf , 6, Leaf)) , 8, ( Node ( Leaf , 9, Leaf )))))

let tree_product t = fold_tree (fun l v r -> l * v * r) 1 t

let tree_flip t = fold_tree (fun l v r -> Node (r, v, l)) Leaf t

let tree_height t = fold_tree (fun l _ r -> 1 + max l r) 0 t

let tree_span t = fold_tree (fun (min_l, max_l) v (min_r, max_r) -> (min min_l (min v min_r), max max_l (max v max_r))) (max_int, min_int) t

let preorder t = fold_tree (fun l v r -> v :: l @ r) [] t

(* let rec print_int_list l = 
  match l with
  | [] -> print_string "\n"
  | h::t -> print_int h; print_string " "; print_int_list t
;;
let rec print_int2 (a, b) = print_int a; print_string " "; print_int b;;

print_int_list (preorder te);;
print_newline();;
print_int (tree_product te);;
print_newline();;
print_int (tree_height te);;
print_newline();;
print_int2 (tree_span te);;
print_newline();;
print_int_list (preorder (tree_flip te));; *)


