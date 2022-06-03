
import Data.List

myInt :: Integer
myInt = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555

double :: Integer -> Integer
double x = x+x


maxim :: Integer -> Integer -> Integer
--maxim :: Ord p => p -> p -> p
maxim x y = 
     if x > y
          then x
          else y

max3 x y z = let
             u = maxim x y
             in maxim u z

               
--max4 :: Integer -> Integer -> Integer -> Integer -> Integer
max4 w x y z = 
     let u = max3 w x y
     in maxim u z