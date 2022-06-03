#include <iostream>
#include <cmath>

using namespace std;

class Vector
{
    int dim;
    int* a;
    friend class Matrice;
    friend class Matrice_oarecare;
    friend class Matrice_patratica;
public:
    Vector()
    {
        dim = 0;
        a = nullptr;
    }
    explicit Vector(int dim)
    {
        this->dim = dim;
        a = new int [dim];
    }

    ~Vector()
    {
        delete [] a;
    }

    Vector (const Vector &v):
        dim {v.dim}
    {
        a = new int [v.dim];
        for(int i = 0; i < v.dim; ++i)
            a[i] = v.a[i];
    }

    Vector & operator = (const Vector & v)
    {
        dim = v.dim;

        if(a != nullptr)
            delete [] a;
        ///dealocarea memoriei vectorului in cazul in care avea ceva salvat in el - memory leak

        a = new int [v.dim];

        for(int i = 0; i < v.dim; ++i)
            a[i] = v.a[i];

        return *this;
    }

    friend istream& operator >> (istream& in, Vector& v)
    {
//        v.a = new int [v.dim];
        for(int i = 0; i < v.dim; ++i)
            in >> v.a[i];
        return in;
    }

    friend ostream& operator << (ostream& out, Vector& v)
    {
        for(int i = 0; i < v.dim; ++i)
            out << v.a[i] << " ";

        return out;
    }

    void Resize(int newSize)
    {
        int* v;
        int mini;

        v = new int [newSize];

        for(int i = 0; i < newSize; ++i)
            v[i] = 0;

        if(newSize < dim)
            mini = newSize;
        else
            mini = dim;

        for(int i = 0; i < mini; ++i)
            v[i] = a[i];

        if(a)
            delete [] a;

        a = v;
        dim = newSize;
    }

};

class Matrice
{
protected:
    Vector* v;

public:
    Matrice()
    {
        v = nullptr;
    }

    Matrice(int lin, int col)
    {
        v = new Vector [lin];
        for(int  i = 0; i < lin; ++i)
            v[i].Resize(col);
    }

    virtual void print(ostream&)=0;

    virtual ~Matrice()
    {
        if(v)
            delete [] v;
    }

};

ostream& operator << (ostream& out, Matrice & m)
{
    m.print(out);

    return out;
}

class Matrice_oarecare: public Matrice
{
    int lin;
    int col;

public:
    Matrice_oarecare(int lin, int col):Matrice(lin,col)
    {
        this->lin = lin;
        this->col = col;
    }

    Matrice_oarecare(const Matrice_oarecare & m):
        lin{m.lin},
        col{m.col}
    {
        v = new Vector [m.lin];
        for(int i = 0; i < m.lin; ++i)
            v[i] = m.v[i];
    }

    Matrice_oarecare & operator = (const Matrice_oarecare & m)
    {
        lin = m.lin;
        col = m.col;

        if(v != nullptr)
            delete [] v;
        ///dealocarea memoriei vectorului in cazul in care avea ceva salvat in el - memory leak
        v = new Vector [lin];
        for(int  i = 0; i < lin; ++i)
            v[i].Resize(col);

        for(int i = 0; i < m.lin; ++i)
            v[i] = m.v[i];

        return *this;
    }

    friend istream& operator >> (istream& in, Matrice_oarecare& m)
    {
        for(int i = 0; i < m.lin; ++i)
            in >> m.v[i];
        return in;
    }

//    friend ostream& operator << (ostream& out, Matrice_oarecare& m)
//    {
//        for(int i = 0; i < m.lin; ++i)
//            out << m.v[i] << "\n";
//
//        return out;
//    }

    void print(ostream& out = cout) override
    {
        for(int i = 0; i < lin; ++i)
            out << v[i] << endl;
    }

    ~Matrice_oarecare() {}

};

class Matrice_patratica: public Matrice
{
    int dim;

public:
    Matrice_patratica(int dim):Matrice(dim, dim)
    {
        this->dim = dim;
    }

    Matrice_patratica(const Matrice_patratica & m):Matrice(m.dim,m.dim)
    {
        dim = m.dim;
        for(int i = 0; i < m.dim; ++i)
            v[i] = m.v[i];
    }

    int matriceTriunghiulara()
    {
        int i, j;
        bool ok_jos = 0, ok_sus = 0;

        for(i = 0; i < this->dim; ++i)
            for(j = i+1; j < this->dim; ++j)
                if(this->v[i].a[j])
                {
                    ok_sus = 1;
                    j = this->dim +1;
                }
        for(i = 0; i < this->dim; ++i)
            for(j = i+1; j < this->dim; ++j)
                if(this->v[j].a[i])
                {
                    ok_jos = 1;
                    j = this->dim +1;
                }
        if(ok_sus == 0 && ok_jos == 0)
            return 0;
        else if(ok_sus == 0 || ok_jos == 0)
            return 1;
        else
            return 2;

    }

    void matriceDiagonala()
    {
        if(matriceTriunghiulara() == 0)
            cout << "Matricea este diagonala.\n";
        else if(matriceTriunghiulara() == 1)
            cout << "Matricea nu este diagonala, este numai triunghiulara.\n";
        else
            cout << "Matricea nici macar nu e triunghiulara.\n";


    }

    void print(ostream& out = cout) override
    {
        for(int i = 0; i < dim; ++i)
            out << v[i] << endl;
//        cout << "Iar determinantul este: " << determinantOfMatrix() << endl;
    }


    Matrice_patratica & operator = (const Matrice_patratica & m)
    {
        dim = m.dim;

        if(v != nullptr)
            delete [] v;
        ///dealocarea memoriei vectorului in cazul in care avea ceva salvat in el - memory leak
        v = new Vector [dim];
        for(int  i = 0; i < dim; ++i)
            v[i].Resize(dim);

        for(int i = 0; i < m.dim; ++i)
            v[i] = m.v[i];

        return *this;
    }

    friend istream& operator >> (istream& in, Matrice_patratica& m)
    {
        for(int i = 0; i < m.dim; ++i)
            in >> m.v[i];
        return in;
    }

//    friend ostream& operator << (ostream& out, Matrice_patratica& m)
//    {
//        for(int i = 0; i < m.dim; ++i)
//            out << m.v[i] << "\n";
//
//        return out;
//    }

    ~Matrice_patratica() {}
};


int main()
{

    Matrice_patratica mP(3);

    cin >> mP;
    mP.print();
    mP.matriceDiagonala();
}
