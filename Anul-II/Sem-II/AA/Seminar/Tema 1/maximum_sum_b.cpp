#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f("date.in");
    int K, s, maximum = 0;

    f >> K;

    while(f >> s)
        if(maximum + s <= K)
            maximum += s;
        else if(maximum < s)
            maximum = s;

    cout << maximum;
}
