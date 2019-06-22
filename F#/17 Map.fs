// 43.3
// Безопасная версия поиска по отображению (Map) 
//let map1 = Map.ofList [(128,"oksana"); (32,"oleg")]
let try_find key m = 
  if Map.containsKey key m = true 
    then 
      //printfn "key found value - %s" (Map.find key m) 
      Some(Map.find key m) 
    else 
      //printfn "key not found"
      None
    
//try_find 128 map1
//try_find 256 map1

