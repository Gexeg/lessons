// 17.1
let rec pow = function
| (s, n) when n <= 0 -> ""
| (s, 1) -> s
| (s, n) -> s + pow(s, n-1)
| _ -> ""

// 17.2
let rec isIthChar = function
  | (s, n, c) when (String.length s)-1 < n -> false
  | (s, n, c) when s.[n] = c -> true
  | _ -> false

// 17.3
let rec occFromIth (s, n, c) = 
  let S = string s
  let rec countChars = function
  | (s, n, c, k) when (String.length s)-1 < n -> k
  | (s, n, c, k) when String.length s <= n -> k
  | (s, n, c, k) when s.[n] = c -> countChars (s, n + 1, c, k + 1)
  | (s, n, c, k) -> countChars (s, n + 1, c, k)
  | _ -> 0
  countChars(S, n, c, 0)

