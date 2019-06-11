// tuple_sum
// перегруженный оператор для складывания кортежей с абстрактными деньгами
let (.+.) x y =
  let (gold1, silver1, cooper1) = x
  let (gold2, silver2, cooper2) = y
  let in_cooper = gold1*240 + gold2*240 + silver1*12 + silver2*12 + cooper1 + cooper2
  let gold_amount = in_cooper / 240
  let silver_amount = (in_cooper % 240) / 12
  let cooper_amount = (in_cooper % 240) % 12
  (gold_amount, silver_amount, cooper_amount)

// tuple minus
// перегруженный оператор для вычитания кортежей с абстрактными деньгами
let (.-.) x y =
  let (gold1, silver1, cooper1) = x
  let (gold2, silver2, cooper2) = y
  let in_cooper = gold1*240 - gold2*240 + silver1*12 - silver2*12 + cooper1 - cooper2
  printfn "%d" in_cooper
  let gold_amount = in_cooper / 240
  let silver_amount = (in_cooper % 240) / 12
  let cooper_amount = (in_cooper % 240) % 12
  (gold_amount, silver_amount, cooper_amount)


// complex numbers
// операторы для работы с комплексными числами
let (.+) x y = 
  let a, b = x
  let c, d = y
  let sum = (a + c, b + d)
  sum

let (.*) x y = 
  let a, b = x
  let c, d = y
  let mult = (a*c - b*d, b*c + a*d)
  mult

let (.-) x y = 
  let a, b = x
  let c, d = y
  let sub = (a - c, b - d)
  sub

let (./) x y =
  let c, d = y
  let div = x .* (c / (c*c+d*d) ,-d/(c*c+d*d))
  div
