// 48.4.1
//Элиминация хвостовой рекурсии
//вариант с параметрами-аккумуляторами
let rec fibo1 (n,n1,n2) =
  match (n,n1,n2) with
    | (n,n1,n2) when n = 0 -> n1
    | (n,n1,n2) when n = 1 -> n2
    | (n,n1,n2) -> fibo1 ((n-1),n2,(n1+n2))

//printfn "%d" (fibo1 (4,0,1))

// 48.4.2 
//Элиминация хвостовой рекурсии
//вариант с continuation passing style
let rec fibo2 cont a = 
  if a <= 2 then cont 1 
  else 
    fibo2 (fun x -> 
      fibo2 (fun y ->  
        cont(x + y)) (a - 1)) (a - 2) 

//printfn "%d" (fibo2 id 6)

// 48.4.3
//Дана функция вызывающая переполнение стека.
//Необходимо переписать её, чтобы избежать исключения при вызове
//let rec bigList n k =
//  if n=0 then k []
//  else bigList (n-1) (fun res -> 1::k(res))

let rec bigList n k =
  if n=0 then k []
  else bigList (n-1) (fun res -> k(1::res))

//printfn "%A" (bigList 2300000 id) 
