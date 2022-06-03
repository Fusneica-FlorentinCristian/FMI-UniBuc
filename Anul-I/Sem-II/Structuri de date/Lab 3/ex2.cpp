//#include <cstdio>
#include <iostream>
using namespace std;

int heap[101];
unsigned sizeH;
unsigned parinte(unsigned x)
{
    return (x - 1) / 2;
}

unsigned fiu_stanga(unsigned x)
{
    return 2 * x + 1;
}

unsigned fiu_dreapta(unsigned x)
{
    return 2 * x + 2;
}

void print()
{
    for (unsigned i = 0; i < sizeH; i++)
        cout << heap[i] << " ";
}

void insert(int x)
{
    if (sizeH < 100)
    {
        unsigned pos = sizeH++;
        heap[pos] = x;
        while (pos > 0 and heap[parinte(pos)] > heap[pos])
        {
            swap(heap[parinte(pos)], heap[pos]);
            pos = parinte(pos);
        }
    }
}

int extract()
{
    int mini = heap[0];
    heap[0] = heap[--sizeH];
    heap[sizeH] = 0;
    unsigned pozitie = 0;
    while (1)
    {
        unsigned mai_mic = pozitie;
        if (fiu_stanga(pozitie) < sizeH and heap[fiu_stanga(pozitie)] < heap[mai_mic])
            mai_mic = fiu_stanga(pozitie);

        if (fiu_dreapta(pozitie) < sizeH and heap[fiu_dreapta(pozitie)] < heap[mai_mic])
            mai_mic = fiu_dreapta(pozitie);

        if (heap[pozitie] > heap[mai_mic])
        {
            swap(heap[pozitie], heap[mai_mic]);
            pozitie = mai_mic;
        }
        else
            break;
    }
    return mini;
}


int main()
{
    int v[16] = { 73, 17, 64, 15, 25, 19, 96, 13, 44, 95, 92, 51, 26, 32, 12};
    for (int i = 0; i < 15; i++)
        insert(v[i]);

    for (int i = 0; i < 15; i++)
    {
        v[i] = extract();

        cout << v[i] << " ";
    }
}
