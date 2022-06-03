#include <iostream>
using namespace std;

class C {
public:
    C(){}
    ~C() {
        cout << "~C";
    }
};
int main()
{
    try {
        throw "exception";
        C c;
    }
    catch (const char* s) {
        cout << s;
    }
    return 0;
}

/*
Când programul execută instrucțiunile de apelare funcțională,
CPU stochează adresa de memorie a instrucțiunii în urma apelului funcțional, copiază argumentele funcției pe stivă și transferă în final controlul în funcția specificată.
CPU apoi execută codul funcției, stochează valoarea returnării funcției într-o locație / registru de memorie predefinită și returnează controlul la funcția de apelare.
Acest lucru poate deveni aerian dacă timpul de execuție al funcției este mai mic decât timpul de comutare de la funcția apelant la funcția apelată (callee).
Pentru funcțiile care sunt mari și / sau îndeplinesc sarcini complexe, funcția generală a apelului funcției este de obicei nesemnificativă în comparație cu perioada de timp necesară funcției.
Cu toate acestea, pentru funcții mici, utilizate frecvent, timpul necesar pentru efectuarea apelului funcției este adesea mult mai mare decât timpul necesar pentru a executa efectiv codul funcției.
Această operație generală apare pentru funcții mici, deoarece timpul de execuție al funcției mici este mai mic decât timpul de comutare.

C ++ oferă o funcție în linie pentru a reduce capătul apelurilor funcționale. Funcția Inline este o funcție care se extinde în linie atunci când este apelată.
Când funcția inline este numită codul întreg al funcției inline este introdus sau înlocuit la punctul de apel al funcției inline. Această înlocuire este realizată de compilatorul C ++ la timp de compilare.
Funcția inline poate crește eficiența dacă este mică.
Sintaxa pentru definirea funcției în linie este:
*/
