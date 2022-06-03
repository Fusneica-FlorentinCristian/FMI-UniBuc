fraza=input("fraza: ")
fraza=fraza.split()
sum=0
for x in fraza:
    if x.isdigit():
        sum+=int(x)
print("\n")
print(sum)