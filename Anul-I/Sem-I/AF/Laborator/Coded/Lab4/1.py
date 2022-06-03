# # a)
#
# def ipotenuza ():
#     a = float(input("a="))
#     b = float(input("b="))
#     return (a**2+b**2)**0.5
#
# print(ipotenuza())


# b) triplete pitagoreice




def triplet (a,b):
    writeMe = open("triplete_pitagoreice.txt",'a')

    if isinstance(((a**2+b**2)**0.5),int):
        writeMe.write(a)
        writeMe.write("\n")
        writeMe.write(b)
        writeMe.write("\n")
        writeMe.write((a**2+b**2)**0.5)
        writeMe.write("\n\n")
        writeMe.close()
    return 0

b = int(input("b="))

for i in range(b):
    triplet(i, b)











# 1. (Modulul math, funcția math.sqrt)
# a) Scrieți o funcție “ipotenuza” care primește ca parametri două numere a și b și furnizează
# ipotenuza triunghiului dreptunghic având catetele de lungimi a și b.
# b) Se citește de la tastatură un număr natural b. Folosind funcția de mai sus, scrieți pe fiecare linie
# din fișierul text “triplete_pitagoreice.txt” câte 3 numere a, b și c, astfel: valoarea lui b este cea
# citită de la tastatură, a este un număr natural mai mic sau egal decât b, iar c este tot un număr
# natural reprezentând ipotenuza triunghiului dreptunghic având catetele a și b. Indicație: Pentru
# un anumit b, trebuie găsite toate valorile posibile pentru a și c care respectă condițiile de mai sus.
# Exemple de triplete pitagoreice (pentru valori diferite ale lui b): (3,4,5), (5,12,13), (8,15,17) etc.