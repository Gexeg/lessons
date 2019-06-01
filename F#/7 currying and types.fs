// 20.3.1
let vat x n =
  float x * (1.0 + (float n /100.0))

// 20.3.2
let unvat n x = 
  float x / float n - 1.0

// 20.3.3
let min f =
  let rec check = function
    | n when f n = 0 -> n
    | n -> check(n + 1)
  check 1

