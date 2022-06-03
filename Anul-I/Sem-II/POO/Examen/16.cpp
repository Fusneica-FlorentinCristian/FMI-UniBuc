#include<iostream>
using namespace std;

class A
{
    int i;
public:
    A(int x=8):i(x) {}
    virtual int f(A a)
    {
        return i+a.i;
    }
};
class B: public A
{
    int j;
public:
    B(int x=-2):j(x) {}
    int f(B b)
    {
        return j+b.j;
    }
};
int main()
{
    int i=20;
    A *o;

    if(i%4)
    {
        A a;
        o=new A(i);
    }
    else
    {
        B b;
        o=new B(i);
    }
    cout<<b->f(*o);
    return 0;
}
