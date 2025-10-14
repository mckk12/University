type 'a nnf =
| NNFLit of bool * 'a
| NNFConj of 'a nnf * 'a nnf
| NNFDisj of 'a nnf * 'a nnf

let rec neg_nnf f = 
  match f with
  | NNFLit (b, a) -> NNFLit (not b, a)
  | NNFConj (f1, f2) -> NNFDisj (neg_nnf f1, neg_nnf f2)
  | NNFDisj (f1, f2) -> NNFConj (neg_nnf f1, neg_nnf f2)
;;

(* neg_nnf (NNFLit (true, 1));; *)
