let fold_left f a xs =
  let rec it xs acc =
    match xs with
    | [] -> acc
    | x :: xs' -> it xs' (f acc x)
  in it xs a

let product xs = fold_left ( * ) 1 xs;;

print_int(product []);;

List.fold_left ( * ) 1 [];;

let rec fold_right f xs acc = 
  match xs with
  | [] -> acc
  | x :: xs' -> f x (fold_right f xs' acc);;