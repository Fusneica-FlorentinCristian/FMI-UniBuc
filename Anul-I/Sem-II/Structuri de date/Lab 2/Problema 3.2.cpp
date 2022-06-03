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
