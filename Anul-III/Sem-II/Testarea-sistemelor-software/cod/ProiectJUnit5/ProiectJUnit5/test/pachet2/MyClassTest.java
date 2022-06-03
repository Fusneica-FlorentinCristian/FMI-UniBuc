// JUnit5
// exemplu Vogella editat
// testare functionala, dar si structurala pt. metoda multiply
// testare functionala pt. metoda produsScalar

package pachet2;
import pachet1.*;
import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class MyClassTest {

    @Test
    public void testExceptionIsThrown() {
        MyClass tester = new MyClass();
        assertThrows(IllegalArgumentException.class, () -> tester.multiply(1000, 5));
    }

    @Test
    public void testMultiply() {
        MyClass tester = new MyClass();
        assertEquals(50, tester.multiply(10, 5));
    }

    /*
    test to kill mutant
     */
    @Test
    public void kill999() {
        MyClass tester = new MyClass();
        assertEquals(999, tester.multiply(999, 1));
    }

    @Test
    public void testAdd() {
        // MyClass tester = new MyClass();
        assertEquals(15, MyClass.add(10, 5));
    }

    /*
    Partitionare clase de echivalenta pt metoda produsScalar
    X_1 = {(x1,x2,x3) | x_i > 0, pt. orice i}
    X_2 = {(x1,x2,x3) | exista i ai x_i <= 0}

    Y_1 = {(y1,y2,y3) | y_i > 0, pt. orice i}
    Y_2 = {(y1,y2,y3) | exista i ai y_i <= 0}

    C_11 = {(x,y) | x in X_1, y in Y_1}
    C_12 = {(x,y) | x in X_1, y in Y_2}
    C_2 = {(x,y) | x in X_2}

    c_11: x = (2,1,1), y = (1,1,1)
    c_12: x = (2,1,1), y = (0,-1,0)
    c_2:  x = (-1,-1,-1), y = (-1,0,0)

    Frontiera:
    c_11: x = (1,1,1), y = (1,1,1)
    c_12: x = (1,1,1), y = (0,0,0)
    c_2:  x = (0,0,0), y = (0,0,0)
    */

    @Test
    public void equivalencePartitiononing() {
        MyClass tester = new MyClass();
        assertEquals(4, tester.produsScalar(2,1,1,1,1,1));
        //assertEquals(-1, tester.produsScalar(2,1,1,0,-1,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(2,1,1,0,-1,0));
        //assertEquals(1, tester.produsScalar(-1,-1,-1,-1,0,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(-1,-1,-1,-1,0,0));
    }

    @Test
    public void boundaryAnalysis() {
        MyClass tester = new MyClass();
        assertEquals(3, tester.produsScalar(1,1,1,1,1,1));
        //assertEquals(0, tester.produsScalar(1, 1,1,0,0,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(1,1,1,0,0,0));
        //assertEquals(0, tester.produsScalar(0,0,0,1,1,1)); // nu e necesar
        //assertEquals(0, tester.produsScalar(0,0,0,0,0,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(0,0,0,0,0,0));
    }

    @Test
    public void categoryPartitioning() {
        MyClass tester = new MyClass();
        assertEquals(4, tester.produsScalar(2,1,1,1,1,1));
        //assertEquals(-1, tester.produsScalar(2,1,1,0,-1,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(2,1,1,0,-1,0));
        //assertEquals(1, tester.produsScalar(-1,-1,-1,-1,0,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(-1,-1,-1,-1,0,0));
        assertEquals(3, tester.produsScalar(1,1,1,1,1,1));
        //assertEquals(0, tester.produsScalar(1, 1,1,0,0,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(1,1,1,0,0,0));
        //assertEquals(0, tester.produsScalar(0,0,0,0,0,0));
        assertThrows(IllegalArgumentException.class, () -> tester.produsScalar(0,0,0,0,0,0));
    }
}