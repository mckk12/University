let ( let* ) xs ys = List.concat_map ys xs

let rec choose m n =
  if m > n then [] else m :: choose (m+1) n

let build_row ps n =
  let max_empty = n - (List.fold_left (+) 0 ps) in
  let rec aux ps n last m_e m_s = (*m_s - max start przeksztalcone pozniej na max_empty, last aby zdecydowac czy powinno byc minimum jedno false*)
    if n > 0 then
      match ps with
      | [] -> [List.init n (fun _ -> false)]
      | x :: xs ->
          let* i = choose last m_s in
          let* ys = aux xs (n-x-i) 1 (m_e-i) (m_e-i) in
          [List.init i (fun _ -> false) @ List.init x (fun _ -> true) @ ys]
    else if ps = [] then [[]] else []
  in
  aux ps n 0 max_empty (max_empty+1-List.length ps)

let build_candidate pss n = (*spec wierszy i dlugosc -> bool list list list*)
  let rec aux pss n = match pss with
    | [] -> [[]]
    | ps :: pss ->
        let* xs = build_row ps n in
        let* ys = aux pss n in
        [xs :: ys]
  in
  aux pss n

let verify_row ps xs = 
  let rec aux ps xs = match ps, xs with
    | [], [] -> true
    | [], x::xs -> if x=false then aux [] xs else false
    | ps, [] -> if ps = [0] then true else false
    | p :: ps, x :: xs -> 
        if p = 0 then
          if x then false else aux ps xs
        else
          if x then aux (p-1 :: ps) xs else aux (p :: ps) xs
  in
  aux ps xs

let verify_rows pss xss = 
  List.for_all2 (verify_row) pss xss

let transpose xss = 
  let rec aux xss = match xss with
    | [] -> []
    | [] :: _ -> aux []
    | (x :: xs) :: xss -> (x :: List.map List.hd xss) :: aux (xs :: List.map List.tl xss)
  in
  aux xss
 

type nonogram_spec = {rows: int list list; cols: int list list}

let solve_nonogram nono =
  build_candidate (nono.rows) (List.length (nono.cols))
  |> List.filter (fun xss -> transpose xss |> verify_rows nono.cols)

let example_1 = {
  rows = [[2];[1];[1]];
  cols = [[1;1];[2]]
}

let example_2 = {
  rows = [[2];[2;1];[1;1];[2]];
  cols = [[2];[2;1];[1;1];[2]]
}

let big_example = {
  rows = [[1;2];[2];[1];[1];[2];[2;4];[2;6];[8];[1;1];[2;2]];
  cols = [[2];[3];[1];[2;1];[5];[4];[1;4;1];[1;5];[2;2];[2;1]]
};;
