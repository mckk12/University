
let parens_ok str =
  let rec check_parens count c_l =
    match c_l with
    | [] -> count = 0
    | '(' :: tl -> check_parens (count + 1) tl
    | ')' :: tl -> count > 0 && check_parens (count - 1) tl
    | _ :: tl -> false
  in
  let char_list = List.of_seq (String.to_seq str) in
  check_parens 0 char_list

