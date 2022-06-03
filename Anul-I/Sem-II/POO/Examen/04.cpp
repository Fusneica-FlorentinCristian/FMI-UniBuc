#include<iostream>

using namespace std;

class A
{
    int x;
public:
    A(int y=0):x(y) {}
    int getx()
    {
        return x;
    };
    A operator+(A* o)
    {
        A r(*this);
        r.x=r.x+o->x-1;
        return r;
    }
};

ostream & operator <<(ostream& o, A a)
{
    o<<a.getx();
    return o;
}

int main()
{
    A o1(103);
    cout<<(o1+&o1);
    return 0;
}
