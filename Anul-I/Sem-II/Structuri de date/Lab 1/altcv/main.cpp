#include <cstdio>

struct pereche
{
    int a,b;
};

struct lista
{
    int info;
    lista *next;
} *prim;


void parcurgere(lista *pointer)
{
    printf("%d ",(*pointer).info);
    //parcurgere(pointer->next);
    if ((*pointer).next!=NULL)
        parcurgere((*pointer).next);
    //parcurgere((&(*pointer))->next);
}

void insert_at_begin(int x)
{
    lista *new_lista= new lista;
    new_lista->info=x;
    new_lista->next=prim;
    prim=new_lista; // my first attrib pointers
}


int main()
{

    pereche T,U,V;
    T.a=4;
    T.b=6;

    printf("\nT.a=%d T.b=%d",T.a,T.b);

    printf("\n&T=%X",&T);
    printf("\n&U=%X",&U);
    printf("\n&V=%X",&V);

    printf("\n\n&T.a=%X",&T.a);
    printf("\n&T.b=%X",&T.b);
    printf("\n\&U.a=n%X",&U.a);
    printf("\n&U.b=%X",&U.b);
    printf("\n\n&V.a=%X",&V.a);
    printf("\n&V.b=%X\n",&V.b);

    lista L,M,N;
    L.info=1;
    L.next=&M;
    M.info=2;
    M.next=&N;
    N.info=3;
    N.next=NULL;

    parcurgere(&L);

    insert_at_begin(7);
    insert_at_begin(8);
    insert_at_begin(9);

    parcurgere(prim);

    return 0;
}
