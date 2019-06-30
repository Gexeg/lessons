// 47.4.1
//Императивное программирование в F# Факториал без рекурсии
let f n = 
    let mutable x = 1
    let mutable k = 1
    while k <= n do
      x <- x * k
      k <- k + 1
    x

//printfn "%d" (f 5)

// 47.4.2
// Число Фибоначчи без рекурсии 
let fibo n = 
  if n < 0 then 0
  elif n = 0 then 0
  elif n = 1 then 1
  else
    let mutable x1 = 0
    let mutable x2 = 1
    let mutable counter = 2
    while counter <= n do
      let temp = x1 + x2
      x1 <- x2
      x2 <- temp
      counter <- counter + 1 
    x2

//printfn "%d" (fibo 4)



