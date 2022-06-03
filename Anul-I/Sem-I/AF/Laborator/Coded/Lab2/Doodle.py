n = int(input("n = "))
Fib = [1, 1]
for i in range(n-2):
    f = Fib[-2] + Fib[-1] # suma ultimelor 2 nr din lista
    Fib.append(f)
print("Primele", n, "numere din sirul Fibonacci sunt:")
print(*Fib[:n+3])