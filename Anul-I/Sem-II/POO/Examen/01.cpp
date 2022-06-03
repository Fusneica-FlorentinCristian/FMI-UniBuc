#include<iostream>

using namespace std;


class A
{
    int x;
public:
    A(int i=2):x(i){}
    int get_x()
    {
        return x;
    }
    A operator+(int);
};

ostream& operator <<(ostream& o, A a)
{
    o<<a.get_x();
    return o;
}

A A::operator+(int i)
{
    return x+i;
}

int main()
{
    A a=33;
    int b=44;
    cout<<a+b<<" "<<b+3;
    return 0;
}
