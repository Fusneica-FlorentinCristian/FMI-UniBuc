#include<iostream>
#include<cmath>
using namespace std;

class Numar_Complex
{
    double real;
    double imag;
public:
    Numar_Complex () = default;
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
    Numar_Complex  operator + (const Numar_Complex & nr)
    {
        Numar_Complex rez;
        rez.imag = imag + nr.imag;
        rez.real = real + nr.real;
        return rez;
    }
    Numar_Complex  operator - (const Numar_Complex & nr)
    {
        Numar_Complex rez;
        rez.imag = imag - nr.imag;
        rez.real = real - nr.real;
        return rez;
    }
    Numar_Complex  operator * (const Numar_Complex & nr)
    {
        Numar_Complex rez;
        rez.real = real * nr.real - imag * nr.imag;
        rez.imag = real * nr.imag + imag * nr.real;
        return rez;
    }
    Numar_Complex  operator / (const Numar_Complex & nr)
    {
        Numar_Complex rez;
        double chestie;
        chestie = nr.real * nr.real + nr.imag * nr.imag;
        if (chestie)
        {
            rez.real = (nr.real * real + imag * nr.imag) / chestie;
            rez.imag = (nr.real * imag - real * nr.imag) / chestie;
        }
        return rez;
    }
    Numar_Complex & operator = (const Numar_Complex & x)
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
    Numar_Complex x(3,5),y(x),z; ///) = new Numar_Complex(3,5);
    cout<<x.getReal()<<endl;
    x.printNumar();
    cout<<endl;
    y.printNumar();
    z = x * y;
    cout<<endl;
    z.printNumar();
    cout<<z.getModul();

    return 0;
}
