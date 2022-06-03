def afisare_matrice(a):
    for linie in a:
        for x in linie:
            print(x, end=' ')  # print('{:4}'.format(x), end= ' ')  
        print()   #!!trebuie () 
def citire(orientat=0,nume_fisier="graf.in"):
    n=0
    a=[]
    
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        a=[[0 for i in range(n)] for j in range(n)]
        #a=[[0]*n for i in range(n)]
        for linie in f: #linie=f.readline(); while linie!='':
            x,y=(int(z) for z in linie.split()) #x,y=map(int,linie.split()) - aplic o functie unei liste
            '''aux=linie.split()
            x=int(aux[0])
            y=int(aux[1])'''
            x-=1; y-=1 
            a[x][y]=1
            if not orientat:
                a[y][x]=1 
                        #linie=f.readline()
          
    return n,a


n,a=citire()
afisare_matrice(a)
