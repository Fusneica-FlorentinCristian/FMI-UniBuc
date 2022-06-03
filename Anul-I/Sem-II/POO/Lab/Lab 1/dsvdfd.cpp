#include<iostream>
#include<cmath>
using namespace std;

class Numar_Complex
{
    double real;
    double imag;
public:
    Numar_Complex ()
    {
        real=0;
        imag=0;
    }
    Numar_Complex (const double real, const double imag):
        real{real},
        imag{imag}
    {

    }
    Numar_Complex (const Numar_Complex & x):
        real{x.real},
        imag{x.imag}
    {

    }
    ~Numar_Complex ()
    {
        real = 0;
        imag = 0;
    }
    Numar_Complex operator + (const Numar_Complex& nr)
    {
        Numar_Complex rez;
        rez.imag = imag + nr.imag;
        rez.real = real + nr.real;
        return rez;
    }
    Numar_Complex operator - (const Numar_Complex& nr)
    {
        Numar_Complex rez;
        rez.imag = imag - nr.imag;
        rez.real = real - nr.real;
        return rez;
    }
    Numar_Complex operator * (const Numar_Complex & nr)
    {
        Numar_Complex rez;
        rez.imag = real * nr.imag + imag * nr.real;
        rez.real = real * nr.real + imag * nr.imag;
        return rez;
    }
    Numar_Complex operator / (const Numar_Complex & nr)
    {
        Numar_Complex rez;
        rez.imag = imag / nr.imag;
        if (nr.real != 0)
            rez.real = real / nr.real;
        return rez;
    }
    Numar_Complex operator = (const Numar_Complex & x)
    {
        real = x.real;
        imag = x.imag;
        return *this;
    }
    void printNumar ()
    {
        if (real == imag && imag == 0)
            cout << 0;
        else if (imag == 0 && real != 0)
            cout << real;
        else if (real == 0 && imag != 0)
            cout << imag << "*i";
        else if (imag < 0)
            cout << real << imag << "*i";
        else
            cout << real << " + " << imag << "*i";
        cout<<endl;
    }
    double getReal ()
    {
        return real;
    }
    double getImag ()
    {
        return imag;
    }
    void setReal (double x)
    {
        real = x;
    }
    void setImag (double x)
    {
        imag = x;
    }
    int getModul ()
    {
        return sqrt (real * real + imag * imag);
    }
};

int main()
{
    Numar_Complex x(3,5), y(0,0), z(5,0), x1(15,2.14), a;
    x.printNumar();
    x.setImag(17);
    x.printNumar();

    int *p,ab;
    ab=56;
    int &xy=ab;
    xy=32;
    cout<<xy<<" ";
    p=&ab;
    cout<<p<<" "<<ab;

    return 0;
}
