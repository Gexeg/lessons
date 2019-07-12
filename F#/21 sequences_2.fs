// 50.2.1
//Те же конструкции, что и в предыдущем упражнении, но с помощью //выражения последовательностей
let fac_seq = seq{
  yield! Seq.initInfinite (fun i -> 
  if i = 0 then 1
  else 
    let rec fact (a,b) = 
      match (a,b) with
        | (_,0) -> 1
        | (a,b) -> a*fact(a-1,b-1)
    fact (i,i))
}

//printfn "%A" fac_seq
// 50.2.2
let seq_seq = seq {
  yield! Seq.initInfinite (fun i ->
  if i % 2 = 0 then i/2
  else (i/2)-i)
}

//printfn "%A" seq_seq
