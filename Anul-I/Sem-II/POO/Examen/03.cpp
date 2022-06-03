#include<iostream>

using namespace std;

class X
{
    int i;
public:
    X(int j=10)
    {
        i=j;
        cout<<i<<" ";
    }
    const int afisare(int j)
    {
        cout<<i<<" ";
        return i+j;
    }
};

int main()
{
    const X O(7),&O2=O, *p=&O2;
    cout<<p->afisare(6);
    return 0;
}
