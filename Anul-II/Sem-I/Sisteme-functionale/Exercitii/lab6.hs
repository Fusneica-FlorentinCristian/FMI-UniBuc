import Data.Char
import Data.List

data Linie = L [Int]
    deriving Show
data Matrice = M [Linie]

verifica :: Matrice -> Int -> Bool
verifica (M cm) n = and (map (verificaLinie1 n) cm)

verificaLinie1 :: Int -> Linie -> Bool
verificaLinie1 n (L cl) = sum cl == n

verificaLinie :: Linie -> Int -> Bool
verificaLinie (L cl) n = sum cl == n

ver :: [Int] -> Int -> Bool
ver xs n = n == sum xs

--if prop(x) then True else False == prop(x)