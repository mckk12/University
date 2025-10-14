(* z4 *)
let rec mem x xs =
  match xs with
  | [] -> false
  | head :: tail ->
    if head = x then
      true
    else
      mem x tail
;;

(* z5 *)
let rec maximum xs =
  match xs with
  | [] -> neg_infinity
  | [x] -> x
  | head :: tail ->
    let tail_max = maximum tail in
    if head > tail_max then
      head
    else
      tail_max
;;

(* z6 *)
let rec suffixes xs =
  match xs with
  | [] -> [[]] 
  | head :: tail ->
    xs :: suffixes tail
;;

(* z7 *)
let rec is_sorted xs =
  match xs with
  | [] | [_] -> true
  | first :: next :: rest -> first <= next && is_sorted (next :: rest)
;;

(* z8 *)
let rec select xs =
  match xs with
  | [] -> failwith "empty"
  | [x] -> (x, [])
  | x :: rest ->
    let (min, rest_without_min) = select rest in
    if x < min then
      (x, rest)
    else
      (min, x :: rest_without_min)
;;

let rec select_sort xs =
  match xs with
  | [] -> []
  | _ -> let (min, rest) = select xs in
  min :: select_sort rest
;;   

(* z9 *)
let split xs =
  let rec split_helper xs acc1 acc2 =
    match xs with
    | [] -> (acc1,  acc2)
    | [x] -> ((x :: acc1), acc2)
    | x1 :: x2 :: rest -> split_helper rest (x1 :: acc1) (x2 :: acc2)
  in
  split_helper xs [] []
;;

let rec merge xs ys =
  match (xs, ys) with
  | ([], _) -> ys
  | (_, []) -> xs
  | (x :: xs_rest, y :: ys_rest) ->
    if x <= y then
      x :: merge xs_rest ys
    else
      y :: merge xs ys_rest
;;

let rec merge_sort xs =
  match xs with
  | [] | [_] -> xs
  | _ ->
    let (left, right) = split xs in
    merge (merge_sort left) (merge_sort right)
;;


(* let example_list4 = [8; 2; 4; 7; 4; 2; 1];;
let result3 = merge_sort example_list4;;
Printf.printf "merge_sort [8; 2; 4; 7; 4; 2; 1] : [%s]\n"
  (String.concat "; " (List.map string_of_int result3)); *)