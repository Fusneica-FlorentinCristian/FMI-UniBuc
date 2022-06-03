
myInt :: Integer
myInt = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555

double :: Integer -> Integer
double x = x+x

main :: IO ()
main = print (double myInt)