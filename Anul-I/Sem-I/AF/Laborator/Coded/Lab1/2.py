L1=int(input("L1="))
L2=int(input("L2="))
a=L1
b=L2
while a>1 and b>1 and a!=b:
    if a<b:
        b-=a
    else:
        a-=b
print(int(L1/a*L2/a)," placi de dimensiune ",a)

# Un meșter trebuie să paveze întreaga pardoseală a unei bucătării cu formă
# dreptunghiulară de dimensiune LL1 × LL2 centimetri, cu plăci de gresie pătrate,
# toate cu aceeași dimensiune. Știind că meșterul nu vrea să taie nici o placă de
# gresie și vrea să folosească un număr minim de plăci, să se determine
# dimensiunea plăcilor de gresie de care are nevoie, precum și numărul lor. De
# exemplu, dacă LL1 = 440 cm și LL2 = 280 cm, atunci meșterul are nevoie de
# 77 de plăci de gresie, fiecare având latura de 40 cm.