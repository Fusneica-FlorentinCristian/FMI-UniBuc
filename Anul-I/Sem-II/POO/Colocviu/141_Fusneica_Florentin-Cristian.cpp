/*
Fusneica Florentin-Cristian, grupa 141
Compilator: -std=c++11
Tutore de laborator: Gusatu Marian
*/

#include <iostream>
#include <vector>
#include <string>
#include <vector>

using namespace std;


/// Clase
class masca
{
public:
    masca() = default;
};

///----------------------------------------------------------------------------------------------->

class chirurgicala: public masca
{
    string protectie, culoare;
    int pliuri;

public:
    chirurgicala();
    chirurgicala(string protectie, string culoare, int pliuri);
    chirurgicala(const chirurgicala &obiect):
        protectie{obiect.protectie},
        culoare{obiect.culoare},
        pliuri{obiect.pliuri}
    {

    }

    ~chirurgicala() = default;

    void citire(istream &in);
    void afisare(ostream &out);
    chirurgicala& operator=(chirurgicala &p);
    friend istream& operator>>(istream&, chirurgicala&);
    friend ostream& operator<<(ostream&, chirurgicala&);

};

///----------------------------------------------------------------------------------------------->

class policarbonata: public masca
{
    const string protectie = "ffp0";
    string culoare, prindere;
    int pliuri;
public:
    policarbonata();
    policarbonata(string prindere, const string protectie, string culoare, int pliuri);
    policarbonata(const policarbonata &obiect):
        culoare{obiect.culoare},
        pliuri{obiect.pliuri},
        prindere{obiect.prindere}
    {

    }

    ~policarbonata() = default;

    void citire(istream &in);
    void afisare(ostream &out);
    policarbonata& operator=(policarbonata &p);
    friend istream& operator>>(istream&, policarbonata&);
    friend ostream& operator<<(ostream&, policarbonata&);


};

///----------------------------------------------------------------------------------------------->

class dezinfectant
{
    double org_ucise;
    vector<string> ingrediente;
    vector<string> suprafete;
    double total_bacterii;


public:
    dezinfectant() = default;
//    dezinfectant(org_ucise, vector v1, vector v2);
    virtual double eficienta();
};

class bacterii: virtual public dezinfectant
{
    const double total_bacterii = 1000000000;
public:
    virtual double eficienta();
};

class fungii: virtual public dezinfectant
{
    const double total_bacterii = 1500000;
public:
    virtual double eficienta();

};

class virusuri: virtual public dezinfectant
{
    const double total_bacterii = 100000000;
public:
    virtual double eficienta();

};

class total: public bacterii, public fungii, public virusuri
{
public:
    double eficienta();
};

istream& operator>>(istream& in, policarbonata& p)
{
    p.citire(in);
    return in;
}

ostream& operator<<(ostream& out, policarbonata& p)
{
    p.afisare(out);
    return out;
}

istream& operator>>(istream& in, chirurgicala& p)
{
    p.citire(in);
    return in;
}

ostream& operator<<(ostream& out, chirurgicala& p)
{
    p.afisare(out);
    return out;
}




///----------------------------------------------------------------------------------------------->
int main()
{
    int n;
    cin >> n;
    vector<masca*> mastiDiverse;

    for (int i = 0; i < n; ++i)
    {
        char optiune;
        cout << "Masti tip policarbonat sau chirurgicale (P / C): ";
        cin >> optiune;

        switch (optiune)
        {
        case 'P':
        {
            policarbonata* s = new policarbonata;
            cin >> *s; // trebuie implementat operatorul de citire
            mastiDiverse.push_back(s);
        }
        case 'C':
        {
            chirurgicala* c = new chirurgicala; // la fel ca sus
            cin >> *c; // operatorul de citire
            mastiDiverse.push_back(c);
        }
        }
    }

    return 0;
}


/// Metode

///----------------------------------------------------------------------------------------------->
// chirurgicale
chirurgicala::chirurgicala()
{
    this->protectie = "Nespecificat";
    this->culoare = "Nespecificat";
    this->pliuri = 0;
}
chirurgicala::chirurgicala(string protectie, string culoare, int pliuri)
{
    this->protectie = protectie;
    this->culoare = culoare;
    this->pliuri = pliuri;
}
void chirurgicala::citire(istream &in)
{
    string x;
    int y;
    cout << "Protectie (ffp1, ffp2, ffp3): ";
    in >> x;
    protectie = x;
    cout << "Culoare: ";
    in >> x;
    culoare = x;
    cout << "Numarul de pliuri: ";
    in >> y;
    pliuri = y;
}
void chirurgicala::afisare(ostream &out)
{
    out<<"Protectie: "<<protectie<<"\n";
    out<<"Culoare: "<<culoare<<"\n";
    out<<"Numar de pliuri: "<<pliuri<<"\n";
}
chirurgicala& chirurgicala :: operator= (chirurgicala &x)
{
    if (this!=&x)
    {
        protectie=x.protectie;
        culoare=x.culoare;
        pliuri=x.pliuri;
    }
    return *this;
}

///----------------------------------------------------------------------------------------------->
// policarbonate

policarbonata::policarbonata()
{
    this->culoare = "Nespecificat";
    this->pliuri = 0;
    this->prindere = "Nespicificat";
}
policarbonata::policarbonata(string prindere = "Nespecificat", const string protectie = "ffp0", string culoare = "Nespecificat", int pliuri = 0)
{
    this->culoare = culoare;
    this->pliuri = pliuri;
    this->prindere = prindere;
}

void policarbonata::citire(istream &in)
{
    string x;
    int y;
    cout << "Protectia este ffp0;\n";
    cout << "Culoare: ";
    in >> x;
    culoare = x;
    cout << "Numarul de pliuri: ";
    in >> y;
    pliuri = y;
    cout << "Tip de prindere: ";
    in >> x;
    prindere = x;
}
void policarbonata::afisare(ostream &out)
{
    out<<"Protectie: "<<protectie<<"\n";
    out<<"Culoare: "<<culoare<<"\n";
    out<<"Numar de pliuri: "<<pliuri<<"\n";
    out << "Tip de prindere: "<<prindere<<endl;

}

policarbonata& policarbonata :: operator= (policarbonata &x)
{
    if (this!=&x)
    {
        culoare=x.culoare;
        pliuri=x.pliuri;
        prindere=x.prindere;
    }
    return *this;
}

///----------------------------------------------------------------------------------------------->
// dezinfectant

//dezinfectant::dezinfectant(double org_ucise = 0, vector<string> v1 = {}, vector<string> v2 = {})
//{
//    this->org_ucise = org_ucise;
//    for(string &i:v1)
//        this->ingrediente.push_back(i);
//
//    for(string &i:v1)
//        this->suprafete.push_back(i);
//}

double dezinfectant::eficienta()
{
    return double(org_ucise/total_bacterii);
}

