open List
  
type 'a symbol =
  | T of string
  | N of 'a

type 'a grammar = ('a * ('a symbol list) list) list

let generate (g : 'a grammar) (s : 'a) : string = failwith "not implemented"

let pol : string grammar =
  [ "zdanie", [[N "grupa-podmiotu"; N "grupa-orzeczenia"]]
  ; "grupa-podmiotu", [[N "przydawka"; N "podmiot"]]
  ; "grupa-orzeczenia", [[N "orzeczenie"; N "dopelnienie"]]
  ; "przydawka", [[T "Piękny "];
                  [T "Bogaty "];
                  [T "Wesoły "]]
  ; "podmiot", [[T "policjant "];
                [T "student "];
                [T "piekarz "]]
  ; "orzeczenie", [[T "zjadł "];
                   [T "pokochał "];
                   [T "zobaczył "]]
  ; "dopelnienie", [[T "zupę."];
                    [T "studentkę."];
                    [T "sam siebie."];
                    [T "instytut informatyki."]]]



  

let expr : unit grammar =
  [(), [[N (); T "+"; N ()];
        [N (); T "*"; N ()];
        [T "("; N (); T ")"];
        [T "1"];
        [T "2"]]]

open Random

let rec generate (grammar : 'a grammar) (symbol : 'a) : string =
  let rec choose_production productions =
    match productions with
    | [] -> failwith "No productions found for the symbol"
    | [production] -> production
    | _ -> List.nth productions (Random.int (List.length productions))
  in
  let rec expand_symbol symbol =
    match symbol with
    | T terminal -> terminal
    | N nonterminal ->
      let productions = List.assoc nonterminal grammar in
      let production = choose_production productions in
      String.concat "" (List.map expand_symbol production)
  in
  expand_symbol (N symbol)