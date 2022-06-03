sir=input("sir=")
sir2=""
s=input("cuvantul care va fi inlocuit:")
t=input("cu cuvantul: ")
sir=sir.split()
for x in sir:
    if x==s:
        sir2+=t
        sir2+=" "
    else:
        sir2+=x
        sir2+=" "
print(sir2)

#3. Scrieți un program care ce să înlocuiască într-o propoziție toate aparițiile ce unui cuvânt s cu un cuvânt t. Atenție, NU se poate utiliza metoda replace! De ce?