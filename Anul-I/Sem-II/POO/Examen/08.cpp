#include<iostream>

using namespace std;

class A
{
    int x;
public:
    A(int &i):x(i){}
    int get_x()
    {
        return x;
    }
    A operator+(int&);
};
ostream & operator<<(ostream& o, A a)
{
    o<<a.get_x();
    return o;
}

A A::operator+(int &i)
{
    A t(i);
    return t;
}


int main()
{
    int b=77, c=9;
    A a(b);
    cout<<a+b+c<<" "<<a+c;
    return 0;
}
