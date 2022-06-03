// lab2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

struct stiva{
int val;
stiva *next;
}*top;

void push(int x) {
    stiva* gigel = new stiva; //alocare spatiu
    gigel->val = x; //atribuire camp1 cu int
    gigel->next = top; //atribuire camp2 cu lista*
    top = gigel; // atribuire top cu lista*
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
