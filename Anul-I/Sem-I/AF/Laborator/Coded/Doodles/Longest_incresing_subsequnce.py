def LIS(v, n):
    maxi = 1
    for i in range(1, n):
        for j in range(i):
            if v[i] > v[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                if lis[i] > maxi:
                    maxi = lis[i]

    print(lis)
    return maxi


n = int(input("n = "))
v = []
lis = [1]*n
for i in range(n):
    v.append(int(input(f"v[{i}] = ")))

x = LIS(v, n)

print(x)

# 8
# 10 22 9 33 21 50 41 60
# output 5
