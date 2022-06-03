n=int(input("n="))
v=[None]*n
p=0
for i in range (n):
    v[i]=float(input())
for x in range (1,n):
    if abs(v[x-1]-v[x])>p:
        p=abs(v[x-1]-v[x])
        a = x
        b = x+1
print("cea mai mare crestere in cele ",n," zile a fost de ",p," intre zilele ",a," si ",b)
