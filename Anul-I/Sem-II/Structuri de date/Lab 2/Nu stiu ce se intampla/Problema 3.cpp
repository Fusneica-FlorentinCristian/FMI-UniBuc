///Problema 3
#include <iostream>
#include <fstream>

using namespace std;

ifstream f("date.in");

struct stiva
{
    int val;
    stiva *next;
}*top;

void push(int x)
{
    stiva* new_lista = new stiva; //alocare spatiu
    new_lista -> val = x; //atribuire camp1 cu int
    new_lista -> next = top; //atribuire camp2 cu lista*
    top = new_lista; // atribuire top cu lista*
}

int pop()
{
    int gigel = -1;
    stiva* bob = top;
    if (top != NULL)
    {
        top = top -> next;
        gigel = bob -> val;
        delete bob;
    }
    return gigel;
}

int main()
{
    int x;
    int i, n;
    f>>n;
    if(n>2)
    cout << "Sunt nevoie de " << n/2 << " fire.\n";
    else if(n == 2)
        cout<<"Este nevoie de un singur fir";
    cout << "Ordinea id-urilor firelor care nu sunt intersectate:";
    for(i = 1; i <= n; ++i)
    {
        f>>x;
        if(top)
            if(x == top -> val)
                cout << " " << pop();
            else
                push(x);
        else
            push(x);
    }
    cout << endl;
    if(top == NULL)
        cout << "Configuratie valida";
    else
        cout << "Configuratie invalida";
}
