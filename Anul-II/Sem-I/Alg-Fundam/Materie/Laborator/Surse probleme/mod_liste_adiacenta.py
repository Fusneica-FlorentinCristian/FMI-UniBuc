def afisare_liste(la):
    for (i,li) in enumerate(la):
        print("{}:".format(i+1), end=' ')
        for x in li:
            print('{}'.format(x+1), end= ' ')
     
        print()    

def citire(orientat=False,nume_fisier="graf.in"):
    n=0
    a=[]
    with open(nume_fisier) as f:
        linie = f.readline()
        n,m=(int(z) for z in linie.split())
        
        la=[[] for i in range(n)]#la=n*[[]] #!!!NU e ok, sunt aceeasi lista
   
        for linie in f:
            x,y=(int(z) for z in linie.split())
            x-=1; y-=1
            la[x].append(y)
            if not orientat:
                la[y].append(x)
         
        
    return n,la




