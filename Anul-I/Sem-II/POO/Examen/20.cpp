#include <iostream>
using namespace std;
class cls
{
    int i;
public:
    cls()
    {
        cout<<"1";
    }
} A;
class cls2: public cls
{
public:
    cls2()
    {
        cout<<"2";
    }
} B;
class cls3: public cls
{
public:
    cls3()
    {
        cout<<"3";
    }
} C;
class cls4: public cls3, public cls2
{
    cls c;
public:
    cls4()
    {
        cout<<"4";
    }
};
int main()
{
    cls4 ob;
    return 0;
}
