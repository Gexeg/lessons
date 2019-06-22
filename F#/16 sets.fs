// 42.3
// Генерируем множество подмножеств длинной k из множества [1..n]
let allSubsets n k =
  let setN =  [1..n] 
  let rec subsets (main, subset, run) = 
    match main,subset,run with
    | (_, subset,_) when Set.count subset = k -> set [subset]
    | (main, subset,_) when List.length main = 0 -> set []
    | (main, subset, run) ->
      let head::tail = main
      set [ yield! subsets (tail,(Set.add head subset), run+ 1);
        yield! subsets (tail,subset, run + 1) ]
    | _ -> set []
  subsets (setN, set [], 1)

//printfn " "
//printfn "%A" (allSubsets 4 2)
