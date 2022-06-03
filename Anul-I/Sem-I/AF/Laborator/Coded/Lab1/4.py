n=int(input("n="))
v=[None]*n
for i in range (n):
    v[i]=float(input())
# for x in v:
#     print(x)
# print(v[0],"\n",v[1])
# p=v[0]-v[1]
# print(p)
p=0
for x in range (1,n):
    if abs(v[x-1]-v[x])>p:
        p=abs(v[x-1]-v[x])
        a=x-1
        b=x
    # print(p)
print("cea mai mare crestere in cele ",n," zile a fost de ",p," intre zilele ",a," si ",b)

# Se citește un șir format din nn numere reale strict pozitive (nn ≥ 2),
# reprezentând cursul de schimb valutar RON/EURO din nn zile consecutive. Să
# se afișeze zilele între care a avut loc cea mai mare creștere a cursului valutar,
# precum și cuantumul acesteia. De exemplu, pentru nn = 6 zile și cursul valutar
# dat de șirul 4.25, 4.05, 4.25, 4.48, 4.30, 4.40, cea mai mare creștere a fost de
# 0.23 RON, între zilele 3 și 4.
# 4.25
# 4.05
# 4.25
# 4.48
# 4.30
# 4.40