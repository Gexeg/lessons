// 40.1
let rec sum (p, xs) = 
  match (p, xs) with
    | (_, []) -> 0
    | (p, [x]) when p(x) = true -> x
    | (p, head::xs) when p(head) = true -> head + sum(p, xs)
    | (p, head::xs) -> sum(p, xs)
    | _ -> 0

//let task x = x < 0
//printfn "  "
//printfn "Сумма элементов списка по условию %d" (sum (task,[1;2;-3;-50;10;12]))

// 40.2.1
let rec count (xs, n) = 
  match (xs, n) with
    | ([],_) -> 0
    | ([x], n) when x = n -> 1
    | (head::xs, n) when head > n -> 0
    | (head::xs, n) when head = n -> 1 + count(xs, n)
    | (head::xs, n) -> count(xs, n)
    | _ -> 0

//printfn "Сколько раз в списке встретится 1 - %d" (count([1;1;2;3;4;4;15], 1))

// 40.2.2
let rec insert (xs, n) = 
  match (xs,n ) with
    | ([x], n) when x < n -> [x; n]
    | ([x], n) when x > n || x = n -> [n; x]
    | (head::xs, n) when head < n -> [head] @ insert(xs, n)
    | (head::xs, n) when head = n || head > n -> [n] @ [head] @ xs
    | _ -> []

//printfn "Вставить элемент в список %A" (insert([1;2;4;5], 6))
//printfn "Вставить элемент в список %A" (insert([1;2;4;5], 0))
//printfn "Вставить элемент в список %A" (insert([1;2;4;5], 4))
//printfn "Вставить элемент в список %A" (insert([1;2;4;5], 3))

// 40.2.3
let rec intersect (xs1, xs2) = 
  match (xs1, xs2) with
    | ([],[]) | ([],_) | (_,[]) -> []
    | (xs1, xs2) -> 
      let rec in_list (element, list) =
        match (element, list) with
          | (element, head::list) when element = head -> element :: in_list(element,list) 
          | (element, head::list) -> in_list(element,list)
          | _ -> []
      let head::tail = xs1
      in_list(head,xs2) @ intersect(tail, xs2)

printfn " "
printfn "%A" ( intersect([1;5;6], [1;1;2;3]) )
 
// 40.2.4
let rec plus (xs1, xs2) = 
  match (xs1,xs2) with
  | ([],[]) | ([],_) | (_,[]) -> xs1 @ xs2 
  | (head1::xs1, head2::xs2) when head1 < head2 -> [head1] @ plus(xs1, head2::xs2)
  | (head1::xs1, head2::xs2) when head1 > head2 -> [head2] @ plus(head1::xs1, xs2)
  | (head1::xs1, head2::xs2) when head1 = head2 -> [head1;head2] @ plus(xs1, xs2)
  | _ -> []

//printfn "сложение 2 списков %A" ( plus([1;5;6], [1;2;3]) )

// 40.2.5
let rec minus (xs1, xs2) = 
  match (xs1, xs2) with
    | (_, []) | ([],_) -> xs1
    | (xs1, head::xs2) ->
        let rec exc_from_list (element, list) =
            match (element, list) with
                | (element, head::list) when element = head -> list
                | (element, head::list) -> [head] @ exc_from_list(element,list)
                | _ -> []
        minus(exc_from_list(head, xs1),xs2)

//printfn "вычитание 2 списков %A" ( minus([1;1;1;5;6], [1;1;2;3]) )

// 40.3.1
let rec smallest = function
  | [] -> 0
  | [x] -> x
  | head1::head2::tail when head1 < head2 || head1 = head2 -> smallest(head1::tail)
  | head1::head2::tail when head1 > head2 -> smallest(head2::tail)
  | _ -> 0

//printfn "наименьший элемент в списке %d" (smallest [5;6;8;11])

// 40.3.2
let rec delete (element, list) = 
    match (element, list) with
        | (element, head::list) when element = head -> list
        | (element, head::list) -> [head] @ delete(element,list)
        | _ -> []

//printfn "удалить первое вхождение элемента в списке %A" (delete (15,[1;15;16;22;19]))

// 40.3.3
let rec sort = function
  | [] -> []
  | x -> 
    let head = smallest(x)
    [head] @ sort(delete(head, x))

//printfn "%A" (sort [5;2;12;13;4])

// 40.4
let rec revrev = function
  | [] -> []
  | xs ->
    let rec rev_chunks = function
      | [] -> []
      | [x] -> [x |> List.rev]
      | head::xs -> (head |> List.rev) :: rev_chunks(xs) 
    rev_chunks(xs) |> List.rev
     
//printfn "%A" (revrev [[1;2;3];[5;4];[7;8;9]]) 

