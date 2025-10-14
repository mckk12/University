(* z1 *)
let rec fib_r n =
  match n with
  | 0 -> 0
  | 1 -> 1
  | x -> fib_r (n - 1) + fib_r (n - 2);;

(* print_int (fib_r 1000);;
print_newline();; *)

let fib_i n = 
  let rec it a b n =
    if n = 0 then a else it b (a + b) (n - 1)
  in it 0 1 n;;
(* print_int (fib_i 7);;
print_newline();; *)

(* z2 *)

let matrix_mult m n =
  let a11, a12, a21, a22 = m in
  let b11, b12, b21, b22 = n in
  (
    a11 * b11 + a12 * b21,
    a11 * b12 + a12 * b22,
    a21 * b11 + a22 * b21,
    a21 * b12 + a22 * b22
  )
;;

let matrix_id () =
  (1, 0, 0, 1)
;;

let rec matrix_expt m k =
  match k with
  | 0 ->  matrix_id ()
  | _ -> 
    matrix_mult m (matrix_expt m (k-1))
;;

let fib_matrix k =
  let m = (1, 1, 1, 0) in
  let f11, f12, f21, f22 = matrix_expt m k in
  f11
;;

(* let fib_result = fib_matrix 5 in
print_endline (string_of_int fib_result);; *)

(* z3 *)

let rec matrix_expt_fast m k =
  if k = 0 then
    matrix_id()
  else if k = 1 then
    m
  else if k mod 2 = 0 then
    let half_pow = matrix_expt_fast m (k / 2) in
    matrix_mult half_pow half_pow
  else
    matrix_mult m (matrix_expt_fast m (k - 1))

let fib_fast k = 
  let m = (1, 1, 1, 0) in
  let f11, f12, f21, f22 = matrix_expt_fast m k in
  f11
;;  

let time_function_call f x =
  let start_time = Sys.time () in
  let _ = f x in
  let end_time = Sys.time () in
  end_time -. start_time
;;

let k_value = 1000 in

let fib_matrix_time = time_function_call fib_matrix k_value in
let fib_fast_time = time_function_call fib_fast k_value in
(* let fib_rec_time = time_function_call fib_r k_value in *)
let fib_iter_time = time_function_call fib_i k_value in

Printf.printf "fib_matrix: %f s\n" fib_matrix_time;
Printf.printf "fib_fast: %f s\n" fib_fast_time;
(* Printf.printf "fib_rec: %f s\n" fib_rec_time; *)
Printf.printf "fib_iter: %f s\n" fib_iter_time;

