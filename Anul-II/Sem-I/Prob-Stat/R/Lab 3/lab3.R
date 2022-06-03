a = matrix(1:12, nrow = 3, byrow = TRUE)

a[1, 2]
a[1,]
a[, 2]
a[c(1, 2), c(1, 2)]

b = 1:4
rbind(a, b)
rbind(b, a)
a

d = 1:3
cbind(a, d)
a
rownames(a)

rownames(a) = c("Ana", "Ionel", "Maria")
a

colnames(a) = c("algebra", "biologie", "chimie", "Mama lui Nistor")
a

dim(a)
t(a)

solve(a)

M = matrix(1:9, nrow = 3)
solve(M)
det(M)

# %*%
M %*% t(M)
M * t(M)

l = list("Ionel", 2, c(1, 4, 7), matrix(1:6, 2))
l

str(l)

li = list(nume = "Ionel", nota = 2, capacitatea = c(1, 4, 7), mat =matrix(1:6, 2))
li
str(li)

str(l[1])

l[[1]]
str(l[[1]])

l[[4]][1, 3]

li$mat[1, 3]
li$mat

li[2] = NULL
li
str(li)
