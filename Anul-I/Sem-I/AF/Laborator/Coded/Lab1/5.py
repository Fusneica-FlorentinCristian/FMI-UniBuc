n=int(input("n="))
v=[None]*n
ok=1
for i in range (n):
    v[i]=float(input())
    if i==0:
        max1=v[i]
    elif ok==1 and v[i]!=max1:
        max2=v[i]
        ok=0
    if ok==0:
        if max2<v[i] and max1!=v[i]:
            if max1<v[i]:
                max2=max1
                max1=v[i]
            else:
                max2=v[i]
if ok==1:
    print("Imposibil")
else:
    print(max1,max2)
