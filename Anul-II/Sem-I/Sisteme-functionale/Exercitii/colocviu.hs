

estePalindrom'ffc :: (Eq a) => [a] -> Bool
estePalindrom'ffc xs = xs == reverse xs

existaPalindrom'ffc :: [String] -> Bool
existaPalindrom'ffc [] = False
existaPalindrom'ffc (x:xs)
    | estePalindrom'ffc x    = True  
    | otherwise = existaPalindrom'ffc xs

existaPalindrom''ffc :: Eq a => [[a]] -> [Bool]
existaPalindrom''ffc xs = [estePalindrom'ffc x | x <- xs] 

verificare'ffc [] = False
verificare'ffc(x:xs)
    | x == True = True
    | otherwise = verificare'ffc xs

existaPalindrom'''ffc :: [[String]] -> [Bool]
existaPalindrom'''ffc = map estePalindrom'ffc