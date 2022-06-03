a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=b**2-4*a*c
if d<0:
    print("nu are radacina")
elif d==0:
    print("are o singura radacia \nx=",float((-b+d**0.5)/2*a))
else:
    print("are doua radacini distincte:\nx1=",float((-b+d**0.5)/2*a))
    print("x2=",float((-b-d**0.5)/2*a))

# Pentru ecuația de gradul doi aa ∗ xx2 + bb ∗ xx + cc = 0, să se citească de la
# tastatură coeficienții a, b, c (numere întregi). Știind formulele dd(dddddddddd) =
# bb2 − 4 ∗ aa ∗ cc și xx1,2 = −bb±√dd
#
# 2∗aa , să se afișeze dacă ecuația nu are nicio rădăcină
# (pentru dd < 0), are o singura rădăcină xx = ⋯ (pentru dd = 0), sau are două
# rădăcini distincte xx1 = ⋯ și xx2 = ⋯ (pentru dd > 0).