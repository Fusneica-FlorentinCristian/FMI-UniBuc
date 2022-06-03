#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream f("date.in");

unsigned int suma_maxima(int K, const vector<unsigned int> valori)
{
    unsigned int maximum = 0;
    vector <unsigned int> sume;
    sume.push_back(0);
    for(unsigned int valoare: valori)
        for(unsigned int suma: sume)
            if(suma + valoare <= K){
                maximum = max(maximum, suma + valoare);
                sume.push_back(suma + valoare);
            }
    return maximum;
}

int main()
{
    int K, val;
    vector <unsigned int> S;

    f >> K;

    while(f >> val)
        S.push_back(val);

    cout << suma_maxima(K, S);


}
