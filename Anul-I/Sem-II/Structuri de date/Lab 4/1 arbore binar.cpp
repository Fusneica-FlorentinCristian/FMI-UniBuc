//1. (3p) Implementati arbore binar de cautare cu operatiile:
//
//- inserarea unei chei x
//- cautarea unei chei x (zice 0/1)
//- afisarea cheilor din arbore dupa SRD (inordine) si RSD (preordine)
//- (+3p) stergerea unei chei x (o aparitie) cu pastrarea proprietatii de arbor binar de cautare

#include <iostream>
using namespace std;

struct nod
{
    int info;
    nod *stanga, *dreapta;
};

// Crearea unui arbore binar stiind cheia (informatia)
nod* nodNou(int valoare)
{
    nod* node = new nod;
    node->info = valoare;
    node->stanga = node->dreapta = nullptr;

    return node;
}

// SRD (inordine) pentru un arbore binar
void SRD(nod *radacina)
{
    if (radacina == nullptr)
        return;

    SRD(radacina->stanga);
    cout << radacina->info << " ";
    SRD(radacina->dreapta);
}

// RSD (preordine) pentru un arbore binar
void RSD(nod *radacina)
{
    if (radacina == nullptr)
        return;

    cout << radacina->info << " ";
    RSD(radacina->stanga);
    RSD(radacina->dreapta);
}

// Functie ajutatoare pentru cautarea maximului din arbore
nod* max(nod* nodMaxim)
{
    while(nodMaxim->dreapta != nullptr)
    {
        nodMaxim = nodMaxim->dreapta;
    }
    return nodMaxim;
}

// Functie recursiva pentru adaugarea unui nod
nod* inserare(nod* radacina, int valoare)
{
    // daca radacina este nula, creaza un nod nou
    if (radacina == nullptr)
        return nodNou(valoare);

    // daca val e mai mica, cauta recursiv la stanga
    if (valoare < radacina->info)
        radacina->stanga = inserare(radacina->stanga, valoare);

    // daca val e mai mare, cauta recursiv la dreapta
    else
        radacina->dreapta = inserare(radacina->dreapta, valoare);

    return radacina;
}


int cauta(nod* radacina, int valoare)
{
    // verificam daca a ajuns la sfarsit si inca nu l-a gasit
    if (radacina == nullptr)
        return 0;
    // verificam daca am gasit valoarea
    else if (valoare == radacina->info)
        return 1;

    // daca e mai mic decat nodul curent, cauta la stanga
    else if (valoare < radacina->info)
        cauta(radacina->stanga, valoare);

    // daca e mai mare, la dreapta
    else if (valoare > radacina->info)
        cauta(radacina->dreapta, valoare);
}

void stergere(nod* &radacina, int valoare)
{
    if (radacina == nullptr)
        return;
    // daca e mai mic decat nodul curent, cauta la stanga
    if (valoare < radacina->info)
        stergere(radacina->stanga, valoare);

    // daca e mai mare, la dreapta
    else if (valoare > radacina->info)
        stergere(radacina->dreapta, valoare);
    else
    {
        // Cazul 1: nu are copii (e frunza)
        if (radacina->stanga == nullptr && radacina->dreapta == nullptr)
        {
            // dealocheaza memoria si schimba pointerul la NULL
            delete radacina;
            radacina = nullptr;
        }

        // Cazul 2: are doi copii
        else if (radacina->stanga && radacina->dreapta)
        {
            // predecesor va lua informatiile nodului cu cea mai mare valoare din stanga
            nod *predecesor = max(radacina->stanga);

            // copiaza valoarea predecesorului in modul curent
            radacina->info = predecesor->info;

            // sterge recursiv predecesorul (va avea maxim un fiu, cel din stanga)
            stergere(radacina->stanga, predecesor->info);
        }

        // Cazul 3: are un singur copil
        else
        {
            // gaseste nodul copil
            nod* child;
            if(radacina->stanga)
                child = radacina->stanga;
            else
                child = radacina->dreapta;

            nod* copie = radacina;

            radacina = child;

            // dealocheaza memoria
            delete copie;
        }
    }
}

int main()
{
    nod* radacina = nullptr;
    int valori[] = { 50, 76, 21, 4, 32, 64, 15, 52, 14, 100, 83, 2, 3, 70, 87, 80 };

    for (int valoare : valori)
        radacina = inserare(radacina, valoare);

    SRD(radacina);
    cout << endl;
    stergere(radacina, 64);
    SRD(radacina);
    cout << endl << cauta(radacina, 50) << " " << cauta(radacina, 64);

    return 0;
}
