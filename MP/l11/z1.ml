let exists f xs =
  try
    List.iter (fun x -> if f x then raise Exit) xs;
    false
  with Exit -> true