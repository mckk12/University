(* module MakeListDict (Key : Map.OrderedType) : DICT with type 'a dict = (Key.t * 'a) list = struct
  type 'a dict = (Key.t * 'a) list
  let empty = []
  let remove k d = List.filter (fun (k', _) -> Key.compare k k' <> 0) d
  let insert k v d = (k, v) :: remove k d
  let find_opt k d = List.find_opt (fun (k', _) -> Key.compare k k' = 0) d |> Option.map snd
  let find k d = List.find (fun (k', _) -> Key.compare k k' = 0) d |> snd
  let to_list d = d
end

module CharListDict = MakeListDict(struct
  type t = char
  let compare = compare *)
(* end) *)

module MakeListDict (M : Map.OrderedType) = struct
  type key = M.t
  type 'a dict = (key * 'a) list
  val empty = 'a dict
end

module CharListDict = MakeListDict(Char)

 
