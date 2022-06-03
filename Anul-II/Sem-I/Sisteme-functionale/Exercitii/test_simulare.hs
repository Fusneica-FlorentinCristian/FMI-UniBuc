import Data.Char ( isAlpha )
import Data.List(sort)
fn2 :: Char -> Bool
fn2 c 
    | not(isAlpha c) = error "error"
    | c `elem` ['a'..'m'] = True
    | c `elem` ['A'..'M'] = True
    | otherwise = False

fn3 :: Char -> Bool
fn3 a = if not(isAlpha a) then error "error" 
        else a `elem` ['a'..'m'] || a `elem` ['A'..'M']

sorter :: (Eq a, Ord a) =>[a] -> [a]
sorter [] = []
sorter [_] = []
sorter v = 
    let (x:y:xs) = sort v
    in if x == y then x:sorter(y:xs) else sorter(y:xs)

-- if x == y then x:sorter(y:xs) else sorter(y:xs)
