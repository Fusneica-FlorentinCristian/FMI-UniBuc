//    #include <cstdio>
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

    int main()
    {
        unsigned v[10] = { 3,	4,	4,	2,	4,	5,	1,	2,	6,	2};
        unsigned maxi = 0;
        for (unsigned i = 0; i < 10; i++)
        {
            if (v[i] > maxi)
            {
                maxi = v[i];
            }
        }
        count_sort(v, 10, ++maxi);
        for (unsigned i = 0; i < 10; i++)
        {
            cout << v[i] << " ";
        }
    }
