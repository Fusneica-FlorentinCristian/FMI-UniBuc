///Problema 2

#include <iostream>
using namespace std;
struct coada
{
    int info;
    coada *penult, *next;
} *prim, *ultim;

void initializer()
{
    prim = NULL;
    ultim = NULL;
}

void push_prim(int x)
{
    coada *p = new(coada);
    p -> info = x;
    p -> penult = NULL;
    p -> next = prim;
    if(prim != NULL)
        prim -> penult = p;
    prim = p;
    if(prim -> next == NULL )
        ultim = prim;
}
void push_ultim(int x)
{
    coada *p = new(coada);
    p -> info = x;
    p -> next = NULL;
    p -> penult = ultim;
    if(ultim != NULL)
        ultim -> next = p;
    ultim = p;
    if(ultim -> penult == NULL)
        prim = ultim;
}
void pop_prim()
{
    coada *p = prim;
    if(prim != NULL)
    {
        if(prim -> next != NULL)
            prim -> next -> penult = NULL;
        prim = prim -> next;
        delete p;
        if(prim == NULL)
            ultim = NULL;
    }
}
void pop_ultim()
{
    coada *p = ultim;
    if(ultim != NULL)
    {
        if(ultim -> penult)
            ultim -> penult -> next = NULL;
        ultim = ultim -> penult;
        delete p;
        if(ultim == NULL)
            prim = NULL;
    }
}
void afisare()
{
    coada *p;
    p = prim;
    while(p)
    {
        cout << p -> info << " ";
        p = p -> next;
    }
    cout << '\n';
}
int main()
{
    initializer();
    push_prim(1);
    push_ultim(2);
    pop_ultim();
    pop_prim();
    push_ultim(3);
    afisare();
    return 0;
}
