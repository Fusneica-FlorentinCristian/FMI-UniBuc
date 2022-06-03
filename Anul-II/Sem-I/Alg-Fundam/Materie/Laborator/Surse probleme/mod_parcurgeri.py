import mod_liste_adiacenta as mla
from collections import deque

def BF(n,la,s=1):
        s-=1  
        viz=[0]*n
        tata=[None]*n
        d=[None]*n
        q = deque()
        parc_bf=[]
        q.append(s)
        viz[s]=1
        d[s]=0
        while len(q)>0:
            x=q.popleft()
            parc_bf.append(x+1)
            for y in la[x]:
                if viz[y]==0:
                      viz[y]=1
                      tata[y]=x
                      d[y]=d[x]+1
                      q.append(y)
                
        return parc_bf,d,tata 
 
def DF(n,la,s=1):
    s-=1;  
    viz=[0]*n
    tata=[None]*n
    d=[None]*n
    parc_df=[]
    d[s]=0
    DFs(n,la,s,viz,tata,d,parc_df)
    return parc_df,d,tata

def DFs(n,la,x,viz,tata,d,parc_df): 
    viz[x]=1
    parc_df.append(x+1)
    for y in la[x]:
        if viz[y]==0:
             tata[y]=x
             d[y]=d[x]+1
             DFs(n,la,y,viz,tata,d,parc_df)
             
def test():
    #test modul
    print("orientat:")
    n,la=mla.citire(True,"grafor.in")
    mla.afisare_liste(la)
    parc_bf,d,tata = BF(n,la,1)
    print("BF(1):",parc_bf,d,tata)
    parc_df,d,tata = DF(n,la,1)
    print("DF(1):",parc_df,d,tata)

    print("neorientat:")
    n,la=mla.citire(False,"graf.in")
    mla.afisare_liste(la)
    parc_bf,d,tata = BF(n,la,1)
    print("BF(1):",parc_bf,d,tata)
    parc_df,d,tata = DF(n,la,1)
    print("DF(1):",parc_df,d,tata)

