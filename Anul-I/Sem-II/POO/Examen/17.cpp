#include<iostream>
using namespace std;

class A
{
protected:
    int nm;
public:
    A(int hbr=1):nm(hbr)
    {
        std::cout<<"?";
    }
    int ha()
    {
        return nm;
    }
    virtual void r() const {};
     ~A()=0;
};
class B: public A
{
    int d;
public:
    B(int b=2):d(b)
    {
        std::cout<<"!!";
    }
    void r(int z)const
    {
        std::cout<<nm<<" "<<z<<"\n";
    }
};
void warranty(const A& am)
{
    am.r();
}
int main()
{
    A ha;
    B un(ha.ha());
    warranty(un);
}
