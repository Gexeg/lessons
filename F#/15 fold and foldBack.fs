// 41.4.1
//let pred1 x = x > 0
let list_filter f xs =
    let folder x acc =
        if f(x)=true then x::acc
        else acc
    List.foldBack folder xs []

//printfn"%A" (list_filter pred1 [1;-2;-4;-6;10]) // [1;10]

// 41.4.2
//let pred2 x = x > 0
let sum (p, xs) = 
    let fb_pred x y  =
      if p(x)=true && p(y)=true then x+y
      elif p(x)=true && p(y)=false then x
      elif p(x)=false && p(y)=true then y
      else 0
    List.foldBack fb_pred xs 0

//printfn "%d"  (sum( pred2, [-2;-4;15;20;1] ) ) //36

// 41.4.3
let revrev xs = 
  let rev lst = List.fold (fun head tail -> tail::head) [] lst
  let folder acc x = 
    let reverse_el = rev x
    reverse_el::acc
  List.fold folder [] xs

//printfn "%A" (revrev [[1;2;3];[4;5;8]]) // [[8;5;4];[3;2;1]]
