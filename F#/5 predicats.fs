// 16.1
let notDivisible (n,m) = m % n = 0 

// 16.2
let  prime x =
  seq { for i = 2 to x/2 do if x % i = 0 then yeld i}
  |> Seq.isEmpty

