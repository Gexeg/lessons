let g n = n + 5 // тип? int -> int

let gg = fun n -> n + 5
 
let h (x,y) = 
  let a = x**2.0
  let b = y**2.0
  let c = a + b
  sqrt c
