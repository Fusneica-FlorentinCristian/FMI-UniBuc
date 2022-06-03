def Thatnos_snap(v):
    if v.isorted():
        return 0
    else:
        return 1


n=int(input("a = "))
v=[0]*n
for i in range(n):
    v[i]=int(input(f"v[{i}] : "))

print(Thatnos_snap(v))