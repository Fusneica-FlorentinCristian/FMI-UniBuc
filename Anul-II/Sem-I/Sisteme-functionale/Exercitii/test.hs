doubleMe x = x + x

test1 = [1,2,3,4,5]

triangles = [(a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]

myLast :: [a] -> a
myLast [] = error "No end for empty lists!"
myLast [x] = x
myLast (_:xs) = myLast xs

myLast' :: [a] -> a
myLast' xs = last xs

myButLast  :: [a] -> a
myButLast  [] = error "No end for empty lists!"
myButLast  [x] = error "No end for lists with one element!"
myButLast  [y,z] = y
myButLast  (_:xs) = myButLast xs

elementAt :: (Int b) => [a] -> b -> a
elementAt [] = error "No end for empty lists!"
elementAt if b <