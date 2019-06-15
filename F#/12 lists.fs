// 34.1
let rec upto n = 
  let rec build_list = function
    | (q,k,n_list) when k = 0 -> n_list 
    | (q,k,n_list) -> build_list(q,k-1,k::n_list)
    | (_,_,_) -> []
  build_list (n, n, [])

// 34.2
let rec dnto n = 
  let rec build_list = function
    | (q,k,n_list) when k = q + 1 -> n_list 
    | (q,k,n_list) -> build_list(q,k+1,k::n_list)
    | (_,_,_) -> []
  build_list (n, 1, [])


// 34.3
let rec even n = 
    let rec build_list = function
        | (q,k,n_list, j) when j = q -> n_list 
        | (q,k,n_list, j) -> build_list(q,k+2,k::n_list, j+1)
        | (_,_,_,_) -> []
    build_list (n, 2, [], 0)

