
readMe =open("numere.txt" ,'r')
variabil = [int(x) for x in readMe.readline().split()]


def min_max(*variabil):
    if variabil[1] >= variabil[0]:
        maxi = variabil[1]
        mini = variabil[0]
    else:
        maxi = variabil[0]
        mini = variabil[1]
    for elem in variabil:
        if elem > maxi:
            maxi = elem
        elif elem < mini:
            mini = elem
    return mini, maxi

print (min_max(variabil))




# 3. (Tratarea excepțiilor)
# a) Să se scrie o funcție “min_max” care primește un număr variabil de parametri (numere
# naturale) și returnează cel mai mic și cel mai mare număr dintre cele primite ca parametri, dacă
# există cel puțin un parametru și dacă toți parametrii sunt numere naturale, sau returnează None
# altfel.
# b) Să se citească tot conținutul fișierului text “numere.txt” și apoi să se afișeze pe ecran rezultatele
# obținute aplicând funcția “min_max” asupra sa. Dacă valoarea returnată de funcția min_max este
# diferită de None, se va scrie în fișierul text “impartire.txt” rezultatul împărțirii valorii maxime din
# fișierul text la cea minimă. Să se trateze excepțiile care pot să apară: nu există fișierul text de
# intrare, nu există drept de scriere pentru fișierul de ieșire, fișierul de intrare conține valori care nu
# sunt numere naturale, împărțire la zero etc.
# Exemplu: Dacă fișierul text “numere.txt” conține: 11 9 31 7 145 5 101 4 80, atunci funcția
# “min_max” va returna (4, 145), iar în fișierul “impartire.txt” se va scrie: 36.25