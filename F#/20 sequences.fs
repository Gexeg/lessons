// 49.5.1
// Формируем последовательность четных чисел
let even_seq = Seq.initInfinite (fun i -> i*2 + 2)

//printfn "%A" even_seq

// 49.5.2
// Последовательность факториалов неотрицательных целых чисел
let fac_seq = Seq.initInfinite (fun i -> 
  if i = 0 then 1
  else 
    let rec fact (a,b) = 
      match (a,b) with
        | (_,0) -> 1
        | (a,b) -> a*fact(a-1,b-1)
    fact (i,i))

//printfn "%A" fac_seq

// 49.5.3
// последовательность 0, -1, 1, -2, 2, -3, 3, ...
let seq_seq = Seq.initInfinite (fun i ->
  if i % 2 = 0 then i/2
  else (i/2)-i)

//printfn "%A" seq_seq
