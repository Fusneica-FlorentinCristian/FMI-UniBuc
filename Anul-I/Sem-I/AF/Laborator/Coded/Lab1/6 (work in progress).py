n=int(input("n="))
v=[0]*10
c=n
max=0
min=0
if n==0:
    print(0,0)
else:
    while c>0:
        y=c%10
        v[y]+=1
        c//=10
w=v.copy()
for x in range(9,-1,-1):
    while w[x]>0:
        max=max*10+x
        w[x]-=1
for x in range(0,10):
    while v[x]>0:
        min=min*10+x
        v[x]-=1
print(min,max)
# 812383