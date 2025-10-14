module type HUFFMAN = sig
  type 'a code_tree
  type 'a code_dict
  val code_tree : 'a list -> 'a code_tree
  val dict_of_code_tree : 'a code_tree -> 'a code_dict
  val encode : 'a list -> 'a code_dict -> int list
  val decode : int list -> 'a code_tree -> 'a list
end

module type DICT = sig
  type ('a, 'b) dict
  val empty : ('a, 'b) dict
  val insert : 'a -> 'b -> ('a, 'b) dict -> ('a, 'b) dict
  val remove : 'a -> ('a, 'b) dict -> ('a, 'b) dict
  val find_opt : 'a -> ('a, 'b) dict -> 'b option
  val find : 'a -> ('a, 'b) dict -> 'b
  val to_list : ('a, 'b) dict -> ('a * 'b) list
end

module ListDict : DICT = struct
  type ('a, 'b) dict = ('a * 'b) list
  let empty = []
  let remove k d = List.filter (fun (k', _) -> k <> k') d
  let insert k v d = (k, v) :: remove k d
  let find_opt k d = List.find_opt (fun (k', _) -> k = k') d |> Option.map snd
  let find k d = List.find (fun (k', _) -> k = k') d |> snd
  let to_list d = d
end

module type PRIO_QUEUE = sig
  type ('a, 'b) pq
  
  val empty : ('a, 'b) pq
  val insert : 'a -> 'b -> ('a, 'b) pq -> ('a, 'b) pq
  val pop : ('a, 'b) pq -> ('a, 'b) pq
  val min_with_prio : ('a, 'b) pq -> 'a * 'b
end

module ListPrioQueue : PRIO_QUEUE = struct
  type ('a, 'b) pq = ('a * 'b) list

  let empty = []
  let rec insert a x q = match q with
  | [] -> [(a, x)]
  | (b, y) :: ys -> if a < b then (a, x) :: q else (b, y) :: insert a x ys
  let pop q = List.tl q
  let min_with_prio q = List.hd q
end


module Huffman (D : DICT) (PQ : PRIO_QUEUE) : HUFFMAN = struct
  type 'a code_tree = Leaf of 'a | Node of 'a code_tree * 'a code_tree
  type 'a code_dict = D.dict

  let code_tree xs =
    let rec build_tree q = match q with
    | [] -> failwith "empty list"
    | [(_, t)] -> t
    | (p1, t1) :: (p2, t2) :: q' -> build_tree (PQ.insert (p1 + p2) (Node (t1, t2)) q')
    in
    let freqs = List.fold_left (fun d x -> match D.find_opt x d with
    | None -> D.insert x 1 d
    | Some n -> D.insert x (n + 1) d) D.empty xs
    in
    let q = List.fold_left (fun q (x, n) -> PQ.insert n (Leaf x) q) PQ.empty (D.to_list freqs)
    in
    build_tree q

  let dict_of_code_tree t =
    let rec aux t rcpref d =
      match t with
      | Leaf x -> ListDict.insert x (List.rev rcpref) d
      | Node (l, r) -> aux l (0 :: rcpref) (aux r (1 :: rcpref) d)
    in aux t [] ListDict.empty

  let encode xs d = List.concat (List.map (fun x -> D.find x d) xs)

  let decode xs t =
    let rec decode' xs t = match t with
    | Leaf x -> (x, xs)
    | Node (l, r) -> match xs with
      | [] -> failwith "empty list"
      | 0 :: xs' -> decode' xs' l
      | 1 :: xs' -> decode' xs' r
      | _ -> failwith "invalid list"
    in
    let rec decode_all xs t = match xs with
    | [] -> []
    | _ -> let (x, xs') = decode' xs t in x :: decode_all xs' t
    in
    decode_all xs t

end