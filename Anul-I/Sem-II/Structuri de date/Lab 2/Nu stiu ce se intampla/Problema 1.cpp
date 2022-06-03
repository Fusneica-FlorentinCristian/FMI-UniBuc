///Problema 1

#include <iostream>
using namespace std;

struct stiva
{
    int val;
    stiva *next;
}*top;

void push(int x)
{
    stiva* new_lista = new stiva; //alocare spatiu
    new_lista->val = x; //atribuire camp1 cu int
    new_lista->next = top; //atribuire camp2 cu lista*
    top = new_lista; // atribuire top cu lista*
}

int pop()
{
    int gigel = -1;
    stiva* bob = top;
    if (top != NULL)
    {
        top = top->next;
        gigel = bob->val;
        delete bob;
    }
    return gigel;
}

int main()
{

    push(1);
    cout<<pop()<<" ";
    push(2);
    push(3);
    cout<<pop();
    cout<<" "<<pop();
}
