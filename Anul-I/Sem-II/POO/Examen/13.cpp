#include<iostream>
using namespace std;

class B
{
    virtual void method()
    {
        cout<<"B::method"<<endl;
    }
public:
    virtual ~B()
    {
        method();
    }
    void baseMethod()
    {
        method();
    }
};
class D: public B
{
    void method()
    {
        cout<<"D::method"<<endl;
    }
public:
    ~D()
    {
        method();
    }
};
int main(void)
{
    B*base = new D;
    base->baseMethod();
    delete base;
    return 0;
}
