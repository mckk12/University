(* module MakeListDict (M : Map.OrderedType) = struct
  type key = M.t
  type 'a dict = 'a Stdlib.Map.Make(M).t
  let insert k v d = Stdlib.Map.Make(M).add k v d
  let find_opt k d = Stdlib.Map.Make(M).find_opt k d
  let find k d = Stdlib.Map.Make(M).find k d
  let to_list d = Stdlib.Map.Make(M).bindings d
end

module CharListDict = MakeListDict(Char) *)