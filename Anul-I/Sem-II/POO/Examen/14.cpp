#include <iostream>
#include <typeinfo>
using namespace std;

class B {
public:
    B() { cout << "B"; }
    virtual ~B() { cout << "~B"; }
};
struct C :public B {
public:
    C() { cout << "C"; }
    ~C() { cout << "~C"; }
};
class D :public C {
public:
    D() { cout << "D"; }
    ~D() { cout << "~D"; }
};


int main() {
    B* pb = new D();
    delete pb;

    return 0;
}
