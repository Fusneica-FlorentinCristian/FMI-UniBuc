def palindrom (x):
    cx = x
    y = 0
    while cx > 0:
        y = y * 10 + cx % 10
        cx = cx // 10
    if y == x:
        return True
    else:
        return False

def verifica_pal(l):
    if len(l) == 0:
        return False
    if palindrom(l[0]) == True:
        return True
    return verifica_pal(l[1:])


lnumere = []
with open("valori.txt", "r") as f:
    s = f.read().split()
    for c in s:
        if "," not in c:
            lnumere.append(int(c))
        else:
            l = c.split(",")
            for nr in l:
                if nr != "":
                    nr = int(nr)
                    lnumere.append(nr)

if verifica_pal(lnumere) == True:
    print("Exista!")
else:
    print("Nu exista!")