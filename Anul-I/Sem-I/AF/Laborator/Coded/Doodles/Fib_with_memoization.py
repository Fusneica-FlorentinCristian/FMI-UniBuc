def fib(n):
    if fib_table[n] == -1:
        if n <= 1:
            fib_table[n] = n
        else:
            fib_table[n] = fib(n - 1) + fib(n - 2)

    return fib_table[n]


n = int(input("n = "))

NIL = -1
fib_table = [NIL] * (n + 1)

x = fib(n)

print(x)
