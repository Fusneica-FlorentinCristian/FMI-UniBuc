/*
exemplu Vogella editat
Specificatie:
a. Sa se calculeze produsul a 2 numere intregi x si y in cazul in care x <= 999.
b. Sa se calculeze suma a 2 numere intregi x si y.
c. Sa se calculeze produsul scalar a 2 vectori x = (x1,x2,x3) si y = (y1,y2,y3), din spatiul euclidian R^3,
in cazul in care xi, yi > 0, intregi, pt. orice i = 1,3.
<x,y> = x1 * y1 + x2 * y2 + x3 * y3
*/

package pachet1;

public class MyClass {

    public int multiply(int x, int y) {
        // the following is just an example
        if (x > 999) {
            throw new IllegalArgumentException("X should be less than 1000");
        }
        System.out.print("Produsul este calculat pt. x mai mic decat 1000\n");
        return x * y;
    }

    public int add(int x, int y) {
        return x + y;
    }

    public int produsScalar(int x1, int x2, int x3, int y1, int y2, int y3) {
        if (x1 <= 0 || x2 <= 0 || x3 <= 0 || y1 <= 0 || y2 <= 0 || y3 <= 0)
        {
            throw new IllegalArgumentException("coordonatele ar trebui sa fie strict pozitive");
        }
        return x1 * y1 + x2 * y2 + x3 * y3;
    }
}