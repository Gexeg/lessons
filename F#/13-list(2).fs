// 39.1
let rec rmodd = function
| [] -> []
| [x] -> []
| head::el1::tail -> el1::rmodd(tail)

// 39.2
let rec del_even =  function
| [] -> []
| [x] when x%2 = 0 -> []
| [x] -> [x]
| head::tail when head%2=0 -> del_even(tail)
| head::tail -> head::del_even(tail)

// 39.3
let rec multiplicity (x,xs) = match (x,xs) with 
| (_,[]) -> 0
| (x,[e]) when e = x -> 1
| (x,[e]) -> 0
| (x,head::xs) when head = x -> 1 + multiplicity(x, xs)
| (x,head::xs) ->  multiplicity(x, xs)
| (_,_) -> 0

// 39.4
let rec split = function
| [] -> [], []
| [x]-> [x],[]
| head1::head2::tail -> 
  let xs1, xs2 = split tail
  (head1::xs1, head2::xs2)

// 39.5
exception DifLength
let rec zip (xs1,xs2) = 
  if (List.length xs1) = (List.length xs2) then 
    match (xs1,xs2) with
      | ([],[]) -> []
      | ([y],[x]) -> [(y,x)]
      | (head1::xs1,head2::xs2) -> [(head1,head2)] @ zip(xs1,xs2)
  else raise DifLength
  
//printfn " "
//printfn "Функция получает элементы с нечетными индексами %A" (rmodd [0..5])
//printfn "Удаляем четные элементы из списка %A" (del_even [0..6])
//printfn "Сколько раз эл встречается в списке %A" (multiplicity (1,[1;1;1;2;4]))
//printfn "разбить список на %A %A" <|| (split [1..11])
//printfn "склеить 2 списка %A"  (zip ([1..11],[1..10]))

