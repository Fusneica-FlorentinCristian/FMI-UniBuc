// lab2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

struct stiva {
    int val;
    stiva* next;
} *top;

void push(int a)
{
    stiva* chestie=top;
    if (chestie == NULL) 
    {
        chestie->val = a;
        chestie = top->next;
    }
    chestie->val = a;
    chestie = top->next;
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
    pop();
    push(2);
    push(3);
}