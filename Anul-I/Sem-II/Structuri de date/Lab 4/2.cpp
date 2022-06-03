//2. (1p) Folositi un arbore binar de cautare ca sa sortati n siruri de caractere. Puteti folosi strcmp din string.h pentru comparare lexicografica intre siruri de caractere.

#include <iostream>
#include <cstring>
using namespace std;

struct nod
{
    char* info;
    nod *stanga, *dreapta;
};

// Crearea unui arbore binar stiind cheia (informatia)
nod* nodNou(char* valoare)
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

// Functie recursiva pentru adaugarea unui nod
nod* inserare(nod* radacina, char* valoare)
{

    // daca radacina este nula, creaza un nod nou
    if (radacina == nullptr)
        radacina = nodNou(valoare);

    // daca val e mai mica, cauta recursiv la stanga
    else if (strcmp(valoare, radacina->info) < 0)
        radacina->stanga = inserare(radacina->stanga, valoare);

    // daca val e mai mare, cauta recursiv la dreapta
    else
        radacina->dreapta = inserare(radacina->dreapta, valoare);

    return radacina;
}


int main()
{
    nod* radacina = nullptr;
    char* valori[] = { "mama", "nistor", "lui", "nistor" };

    for (char* valoare : valori)
        radacina = inserare(radacina, valoare);

    SRD(radacina);
    cout << endl;
    RSD(radacina);

    return 0;
}
