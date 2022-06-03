#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <tuple>
using namespace std;


class farmacie
{
protected:
    string denumire;
    int angajati;
    double profit;

public:
    farmacie() = default;
    farmacie(string denumire, int angajati, double profit)
    {
        this->denumire = denumire;
        this->angajati = angajati;
        this->profit = profit;
    }

    farmacie(const farmacie &farm):
        denumire{farm.denumire},
        angajati{farm.angajati},
        profit{farm.profit}
    {

    }

    virtual ~farmacie() = default;

    farmacie & operator = (const farmacie & x)
    {
        denumire = x.denumire;
        angajati = x.angajati;
        profit = x.profit;

        return *this;
    }

    virtual void read(istream& in)
    {
        in >> denumire >> angajati >> profit;
    }

    virtual void print(ostream& out = cout) const
    {
        out << "Denumire farmacie: " << denumire << "\nNumar angajati: " << angajati << "\nProfit: " << profit;
    }

    void insertDenumire(string denumire)
    {
        this->denumire = denumire;
    }

    void insertAngajati(int angajati)
    {
        this->angajati = angajati;
    }

    void insertProfit(double profit)
    {
        this->profit = profit;
    }
};

istream& operator >> (istream& in, farmacie& x)
{
    x.read(in);
    return in;
}

ostream& operator << (ostream& out, const farmacie & x)
{
    x.print(out);

    return out;
}


class farmacieOnline: public farmacie
{
//    string web;
//    int nr_vizitatori;
//    double discount;
    tuple <string, int, double> far;
public:

    farmacieOnline(string web = "", int nr_vizitatori = 0, double discount = 0, string denumire = "-", int angajati = 0, double profit = 0)
        :farmacie(denumire, angajati, profit)
    {
        get<0>(this->far) = web;
        get<1>(this->far) = nr_vizitatori;
        get<2>(this->far) = discount;
    }

    farmacieOnline(const farmacieOnline &farm): farmacie(farm),
        far{farm.far}
    {}

    ~farmacieOnline() = default;

    farmacieOnline & operator = (const farmacieOnline & x)
    {
        denumire = x.denumire;
        angajati = x.angajati;
        profit = x.profit;
        this->far = x.far;

        return *this;
    }


    void read(istream& in) override
    {
        this->farmacie::read(in);
        in >> get<0>(far) >> get<1>(far) >> get<2>(far);
    }

    void print(ostream& out = cout) const override
    {
        this->farmacie::print(out);
        out << "\nSite-ul web: " << get<0>(far)
            << "\nNumar de vizitatori site: " << get<1>(far)
            << "\nDiscount oferit prin site: " << get<2>(far) << "%";
    }

    int getNrVizitatori()
    {
        return get<1>(this->far);
    }

    void insertWeb(string web)
    {
        get<0>(this->far) = web;
    }
    void insertNrVizitatori(int nr_vizitatori)
    {
        get<1>(this->far) = nr_vizitatori;
    }
    void insertDiscount(double discount)
    {
        get<2>(this->far) = discount;
    }

};



template <class T>
class GestionareFarmacii
{
    int index;
    vector <T> v;
    static int contor;
    const int id; // = 0;
public:
    GestionareFarmacii():
        id{contor}
    {
        contor++;
        index = 0;
    }

    GestionareFarmacii(T farm):
        id{contor}
    {
        contor++;
        v.push_back(farm);
        index = 1;
    }

    GestionareFarmacii(const GestionareFarmacii &farm):
        index{farm.index},
        v{farm.v},
        id{farm.contor}
    {
        contor++;
    }

    int getId() const
    {
        return this->id;
    }

    void addFarmacie(T farmac)
    {
        v.push_back(farmac);
        index++;
    }

    int getNumarFarmacii()
    {
        return this->index;
    }

    T getFarmacie(int index)
    {
        try
        {
            if(index == 0)
                throw 0;
            else if(index < 0)
                throw -1;

            return v[index-1];
        }
        catch(int x)
        {
            T dummyFarmacie;
            return dummyFarmacie;
        }
    }

};

template <class T>
int GestionareFarmacii <T> :: contor = 1;


template <>
class GestionareFarmacii <farmacieOnline>
{
    int index;
    vector <farmacieOnline> v;
    static int contor;
    const int id;
public:
    GestionareFarmacii():
        id{contor}
    {
        contor++;
        index = 0;
    }

    GestionareFarmacii(farmacieOnline farm):
        id{contor}
    {
        contor++;
        v.push_back(farm);
        index = 1;
    }

    GestionareFarmacii(const GestionareFarmacii &farm):
        index{farm.index},
        v{farm.v},
        id{farm.contor}
    {
//        contor++;
    }

    int getId() const
    {
        return this->id;
    }

    int nrVizitatori()
    {
        int total = 0;
        for(farmacieOnline &x: this->v)
            total += x.getNrVizitatori();
        return total;
    }

    void addFarmacie(farmacieOnline farmac)
    {
        v.push_back(farmac);
        index++;
    }

    GestionareFarmacii operator += (farmacieOnline *farmac)
    {
        addFarmacie(*farmac);

        return *this;
    }

    GestionareFarmacii operator += (farmacieOnline farmac)
    {
        addFarmacie(farmac);

        return *this;
    }

    farmacieOnline getFarmacie(int index)
    {
        try
        {
            if(index == 0)
                throw 0;
            else if(index < 0)
                throw -1;

            return v[index-1];
        }
        catch(int x)
        {
            farmacieOnline dummyFarmacie;
            return dummyFarmacie;
        }
    }

    int getNumarFarmacii()
    {
        return this->index;
    }
};
//
template <>
int GestionareFarmacii <farmacieOnline> :: contor = 1;

int main()
{
    farmacie x("mancare", 4, 2000);
    farmacie a(x);
    GestionareFarmacii <farmacie> xx(x), yy;
    vector <farmacieOnline> v;
    farmacieOnline y("http://site1.com", 5, 12), z("http://site2.com", 17, 1, "fara mancare", 0, 9999);
    GestionareFarmacii <farmacieOnline> zz;
    v.push_back(y);
    v.push_back(z);

//    for(farmacieOnline &i: v)
//        cout << i << endl << endl;
//
//    cout << a << endl << endl;

    farmacieOnline *p = new farmacieOnline;

    xx.addFarmacie(a);

    zz.addFarmacie(y);
    cin >> *p;
    zz += p;

    zz += y;
    zz += z;

    cout << "\n" << zz.nrVizitatori() << endl ;
    cout << zz.getNumarFarmacii() << " " <<xx.getNumarFarmacii();

    cout << endl << endl << endl;
}
