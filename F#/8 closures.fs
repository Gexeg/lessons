// 21 closures
let curry in_function = function arg1 -> function arg2 -> in_function(arg1,arg2)

let uncurry in_function = function (x,y) -> (in_function x) y

