// 17.1
let rec pow = function
| (s, 1) -> s
| (s, n) -> s + pow(s, n-1)

// 17.2
let rec isIthChar (s, n, c) =
  let S = string s
  S.[n] = c

// 17.3
let rec occFromIth (s, n, c) = 
  let S = string s
  let rec countChars = function
  | (s, n, c, k) when String.length s <= n -> k
  | (s, n, c, k) when s.[n] = c -> countChars (s, n + 1, c, k + 1)
  | (s, n, c, k) -> countChars (s, n + 1, c, k)
  countChars(S, n, c, 0)
