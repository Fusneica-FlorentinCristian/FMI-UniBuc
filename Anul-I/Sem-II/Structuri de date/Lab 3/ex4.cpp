#include <iostream>
using namespace std;

void count_sort(unsigned* v, unsigned n, unsigned mask, unsigned grupa=0)
{
    unsigned trunc = 1;
    while (grupa--)
        trunc *= mask;

    unsigned range = mask;
    unsigned* index = new unsigned[range];

    for (unsigned i = 0; i < range; i++)
        index[i] = 0;

    for (unsigned i = 0; i < n; i++)
        index[v[i] / trunc % mask]++;

    for (unsigned i = 1; i < range; i++)
        index[i] += index[i - 1];

    unsigned* newList = new unsigned[n];

    for (unsigned j = 0; j < n; j++)
    {
        unsigned i = n - j - 1;
        newList[index[v[i] / trunc % mask] - 1] = v[i];
        index[v[i] / trunc % mask]--;
    }
    for (unsigned i = 0; i < n; i++)
        v[i] = newList[i];

    delete[] newList;
    delete[] index;
}

void rsort(unsigned* v, unsigned n, unsigned mask)
{
    unsigned groups = 0; // of log10(mask)digits or log2(mask)bits
    {
        unsigned maxi = 0;
        for (unsigned i = 0; i < n; i++)
            if (v[i] > maxi)
                maxi = v[i];

        while (maxi)
        {
            groups++;
            maxi /= mask;
        }
    }
    for (unsigned grupa = 0; grupa < groups; grupa++)
        count_sort(v, n, mask, grupa);

}

int main()
{

    unsigned v[15] = {734,	639,	45,	289,	424,	567,	926,	271,	270,	38,	769,	409,	382,	366,	517};
    rsort(v, 15, 15);

    for (unsigned i = 0; i < 15; i++)
        cout << v[i] << " ";

}
