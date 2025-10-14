let build_list n f = 
  let rec it i = 
    if i = n then []
    else f i :: it (i+1)
  in
  it n
;;
let negatives n = build_list n (fun x -> -x);;

let reciprocals n = build_list n (fun x -> 1.0 /. float_of_int x);;

let evens n = build_list n (fun x -> 2 * x);;

let identityM n = build_list n (fun x -> build_list n (fun y -> if x = y then 1 else 0));;

let rec print_int_list l = 
  match l with
  | [] -> print_string "\n"
  | h::t -> print_int h; print_string " "; print_int_list t
;;
let rec print_float_list l = 
  match l with
  | [] -> print_string "\n"
  | h::t -> print_float h; print_string " "; print_float_list t
;;

print_int_list (negatives 10);;
print_newline ();;
print_float_list (reciprocals 10);;
print_newline ();;
print_int_list (evens 10);;
print_newline ();;
print_int_list (List.nth (identityM 3) 0);;
print_int_list (List.nth (identityM 3) 1);;
print_int_list (List.nth (identityM 3) 2);;
