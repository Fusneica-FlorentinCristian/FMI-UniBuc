# character
x <- "test"
typeof(x)

# numeric
y <- 4.3
typeof(y)


# integer
z = 3L
typeof(z)

#logical
t = TRUE
typeof(t)


# complex

vector("character", length = 10)
character(10)
numeric(10)
logical(5)

a = c(2, 3)
a = c(a, 4)
a = c(1, a)

z1 <- c(2.5, TRUE, FALSE, F, T, 3L, logical(5))

1:10
1.5:10
10:1

z2 <- seq(2, 19, by = 2) # sequence generation
seq(2, 19, length.out = 100)
?seq

rep(1, 5) #replicate elements of vectors and lists
rep(1:4, 5)
rep(1:3, 1:3)
?rep

a = 1:10
b = 5

a + b
a - b
a * b
a / b

b=11:30
a + b
a - b
a * b
a / b

x = 1:10
y = log(x)

min(x)
max(x)
sum(x)
prod(x)
length(x)

unique(c(1,2,1,3,1,2))
table(c(1,2,1,3,1,2))
?table

sex = rep(c("M", "F"), c(5, 9))
frecventa = table(sex)
frecventa

x = 1:10
# []
x[c(1, 3, 7)]
x[-5]
x[-c(1, 3, 4)]

x >= 3
x != 5

x[x > 3]
x[x > 8 | x < 2]
x[x %in% c(2, 6, 9)]
x[x > 3 & x < 9]
x[(x > 3) && (x < 9)]

paste("sirul 1", "sirul 2")

paste0("sirul 1", "sirul 2")

args(paste)
args(plot)

for(i in letters){
  print(i)
}

x= letters

for(i in seq_along(x)){
  print(x[i])
}

?outer
M1 = matrix(nrow = 10000, ncol = 10000)

for(i in 1:nrow(M1)){
  for(j in 1:ncol(M1)){
    M1[i, j] = i/cos(j^2)
  }
}

f1 = function(x, y){
  x / cos(y^2)
}

x = 1:10000
y = 1:10000

M2 = outer(x, y, FUN = f1)
identical(M1, M2)
rm(M1, M2)

?rm

?plot

x = seq(-pi, pi, length.out = 100)
y = cos(x)

plot(x)
plot(y)

plot(x, y, type = "l")
plot(x, y, type = "b")
plot(x, y, type = "p", 
     main = "Titlul primului grafic",
     xlab = "Abscisa",
     ylab = "Ordonata",
     col = "blue",
     lty = 2,
     lwd = 2,
     bty = "n",
     pch = 10)


# o functie pe ramuri

# sin(x^2 + 1)/(log(x^3 - 2)), x > 2
# cos(2x - 3) + 7e^x
