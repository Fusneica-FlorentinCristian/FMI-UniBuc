#include<iostream>

using namespace std;

class A
{
    static int x;
    const int y;
public:
    A(int i):

        y(i+3)
    {
        x=i;
    }
    int put_x(A a)
    {
        return x+a.y;
    }
};

int A::x=8;





int main()
{
    A a(2);
    cout<<a.put_x(26);
    return 0;
}
