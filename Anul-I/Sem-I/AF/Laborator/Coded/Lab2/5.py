# ord(char) => numarul ASCII
# chr(num) => caracterul reprezentat de num
# ASCII: 65-95 <=> A-Z
#        97-122 <=> a-z
k=int(input("k="))
while k<0:
    k=input("Introduceti k pozitiv: ")
text2=""
x=int(input("Scrieti 1 pentru criptare, 2 pentru decriptare, 3 pentru amandoua: "))
if x==1 or x==3:
    text=input("Textul dorit pentru criptare: ")
    for i in text:
        if ord(i)>=65 and ord(i)<=90:
            y = ord(i)
            y -= 65
            y += k
            y %= 26
            y += 65
            z = chr(y)
        elif ord(i)>=97 and ord(i)<=122:
            y = ord(i)
            y -= 97
            y += k
            y %= 26
            y += 97
            z = chr(y)
        else:
            z = i
        text2+=z
    print(text2)
text2=""
if x==2 or x==3:
    text = input("Textul dorit pentru decriptare: ")
    k %= 26
    for i in text:
        if ord(i)>=65 and ord(i)<=90:
            y = ord(i)
            y -= 65
            if y - k < 0:
                y += 26 - k
            else:
                y -= k
            y += 65
            z = chr(y)
        elif ord(i)>=97 and ord(i)<=122:
            y = ord(i)
            y -= 97
            if y - k < 0:
                y += 26 - k
            else:
                y -= k
            y += 97
            z = chr(y)
        else:
            z = i
        text2 += z
    print(text2)