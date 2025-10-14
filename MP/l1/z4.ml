let f x y z =
  if x <= y && x <= z then y * y + z * z else (if y <= z && y <= x then x * x + z * z else y * y + x * x);;

print_int(f 2 3 5);;
