// 34.1
let upto n = 
  let rec build_list (q,k,n_list) = match (q,k,n_list) with
    | (q,k,n_list) when k = 0 -> n_list 
    | (q,k,n_list) -> build_list(q,k-1,k::n_list)
    | (_,_,_) -> []
  build_list (n, n, [])

// 34.2
let dnto n = 
  let rec build_list (q,k,n_list) = match (q,k,n_list) with
    | (q,k,n_list) when k = q + 1 -> n_list 
    | (q,k,n_list) -> build_list(q,k+1,k::n_list)
    | (_,_,_) -> []
  build_list (n, 1, [])

// 34.3
let even n = 
    let rec build_list (q,k,(n_list: 'T list)) = match (q,k,n_list) with
        | (q,k,n_list) when n_list.Length = q -> n_list 
        | (q,k,n_list) -> build_list(q,k+2,k::n_list)
        | (_,_,_) -> []
    build_list (n, 2, [])
