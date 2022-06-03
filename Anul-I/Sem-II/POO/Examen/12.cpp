#include <iostream>

using namespace std;
class C {
    int x;
  public:
    C(int x=0):x(x) {}
    operator int() {
        return x;
    }
};
int main() {
    C *arr=new C[12]{2020};
    for(int i; i<12; i++)cout<<arr[i];
    return 0;
}
