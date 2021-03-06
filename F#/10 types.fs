type TimeOfDay = { hours: int; minutes: int; f: string }

let (.>.) x y = match (x,y) with
  | (x,y) when x.f="PM" && y.f="AM" -> true
  | (x,y) when x.f="AM" && y.f="PM" -> false
  | (x,y) when x.hours > y.hours -> true
  | (x,y) when x.hours = y.hours && x.minutes > y.hours -> true
  | _ -> false
