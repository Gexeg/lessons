// Знакомство с ленивыми вычислениями
// Тип данных, который принимает либо пустое значение,
// либо возвращает элемент и оставшуюся часть вычисления
type 'a cell = Nil | Cons of 'a * Lazy<'a cell>

//функция получает значение текущего этапа
let hd (s : 'a cell) : 'a =
  match s with
    Nil -> failwith "hd"
  | Cons (x, _) -> x

//функция получает еще не выполненный "хвост" текущего этапа
let tl (s : 'a cell) : Lazy<'a cell> =
  match s with
    Nil -> failwith "tl"
  | Cons (_, g) -> g

// Проверочная функция, генерирующая бесконечную последовательность 
// числе с 0.
//let rec nat (n:int) : 'a cell = Cons (n, lazy(nat(n+1)))
//let n0 = nat 0

// 51.3
let rec nth (s : 'a cell) (n : int) : 'a = 
  let rec n_el (s, n, k) = match (s,n,k) with
    | (_, n, k) when n < k -> 0
    | (s, n, k) when k = n -> hd <| s
    | (s, n, k) -> 
    //Чтобы передвинуться на шаг вперед необходимо сначала 
    //Получить еще не выполненный хвост и провести в нем вычисления
      let next_step = (tl s).Force()
      n_el(next_step, n, k+1)
  n_el (s, n, 0)

//printfn ""
//printfn "%A" <| (nth n0 30000)
