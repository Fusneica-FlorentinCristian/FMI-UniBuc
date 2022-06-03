/*///Pb 1 (2p) Implementati o stiva cu operatii push si pop folosind o lista.
/// Push va insera elemente la inceputul listei si pop va sterge elemente de la inceputul listei.
#include <iostream>
using namespace std;
struct stiva{
    int info;
    stiva *next;

}*varf;

void init()
{varf=NULL;}

void push(int x)
{
    stiva *p;
    p=new(stiva);
    p->info=x;
    p->next=varf;
    varf=p;
}
int pop()
{
    stiva *p=varf;

    if(varf!=NULL)
        {
        varf=varf->next;
        delete p;
        }

}
void afisare()
{
    stiva *p;
    p=varf;
    while(p){
        cout<<p->info<<" ";
        p=p->next;
    }
    cout<<'\n';
}
int main()
{   init();
    push(1);
    pop();
    push(2);
    push(3);
    afisare();
}
*/
///Pb 2
/// la ambele capete (double ended queue - dequeue):

#include <iostream>
using namespace std;
struct coada{

    int info;

    coada *prev, *next;

} *prim, *ultim;
void init()
{prim=NULL;
 ultim=NULL;}

void pushleft(int x){
    coada *p=new(coada);
    p->info=x;
    p->prev=NULL;
    p->next=prim;
    if(prim!=NULL)
        prim->prev=p;
    prim=p;
    if(prim->next==NULL )
        ultim=prim;
}
void pushright(int x){
    coada *p=new(coada);
    p->info=x;
    p->next=NULL;
    p->prev=ultim;
    if(ultim!=NULL)
        ultim->next=p;
    ultim=p;
    if(ultim->prev==NULL)
        prim=ultim;
}
void popleft(){
    coada *p=prim;
    if(prim!=NULL){
        if(prim->next!=NULL)
            prim->next->prev=NULL;
        prim=prim->next;
        delete p;
        if(prim==NULL)
            ultim=NULL;
    }
}
void popright(){
    coada *p=ultim;
    if(ultim!=NULL){
        if(ultim->prev)
            ultim->prev->next=NULL;
        ultim=ultim->prev;
        delete p;
        if(ultim==NULL)
            prim=NULL;
    }
}
void afisare(){
    coada *p;
    p=prim;
    while(p){
        cout<<p->info<<" ";
        p=p->next;
    }
    cout<<'\n';
}
int main()
{init();
 pushleft(1);
 pushright(2);
 popright();
 popleft();
 pushright(3);
 afisare();
return 0;
}
/*
///Pb 3. (Problema cu stivă 2p) Fie un număr par n de tăruși distribuiți echidistant pe un cerc numerotați de la 1 la n (vezi figura).
///Țărușii trebuie legați cu fire metalice în așa fel încât aceste fire să nu se intersecteze.
#include <iostream>
#include <fstream>
using namespace std;
ifstream f("date.in");
struct stiva{
    int info;
    stiva *next;

}*varf;

void init()
{varf=NULL;}

void push(int x)
{
    stiva *p;
    p=new(stiva);
    p->info=x;
    p->next=varf;
    varf=p;
}
void pop()
{
    stiva *p=varf;

    if(varf!=NULL)
        {
        varf=varf->next;
        delete p;
        }

}
int x;
int main()
{
init();
while(f>>x)
  {if(varf)
    {if(x==varf->info)
        pop();
     else
        push(x);
    }
   else push(x);
  }
if(varf==NULL)
    cout<<"da";
else
    cout<<"nu";
///Pentru exemplul valid 1 2 2 1 3 3 4 4

return 0;
}

///Pb 4. (Problema cu coadă 2p) Spunem ca o imagine digitala binara M este o matrice de m x m elemente (pixeli) 0 sau 1.
/// Un element a al matricei este adiacent cu b, daca b se afla deasupra, la dreapta, dedesubtul, sau la stanga lui a in imaginea M.
#include <iostream>
#include <fstream>
using namespace std;
ifstream f("date.in");
struct coada{

    int x,y;

    coada *prev, *next;

} *prim, *ultim;
void init()
{prim=NULL;
 ultim=NULL;}

void push(int x){
    coada *p=new(coada);
    p->info=x;
    p->prev=NULL;
    p->next=prim;
    if(prim!=NULL)
        prim->prev=p;
    prim=p;
    if(prim->next==NULL )
        ultim=prim;
}

void pop()
{
    coada *p=ultim;

    if(ultim!=NULL)
        {ultim->prev->next=NULL;
        ultim=ultim->prev;
        delete p;
        }

}

int main()
{init();
 while(f>>x && f>>y)
 {if(prim)
    {push()

    }

 }
return 0;
}
*/





