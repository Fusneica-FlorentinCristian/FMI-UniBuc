s1=input("s1=")
s2=input("s2=")
if len(s1)!=len(s2):
    print("nu")
else:
    for i in s1:
        if i in s2:
            s2=s2.replace(i,"",1)
        else:
            print("nu")
            break
    else:
        print("anagrame")
# emerit
# treime