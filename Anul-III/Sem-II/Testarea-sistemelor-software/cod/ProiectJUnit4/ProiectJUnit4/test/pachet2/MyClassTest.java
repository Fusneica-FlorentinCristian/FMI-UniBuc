// JUnit4
// exemplu Vogella editat
// testare functionala, dar si structurala pt. metoda multiply
// testare functionala pt. metoda produsScalar

package pachet2;
import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.SystemOutRule;
import pachet1.*;

import static org.junit.Assert.assertEquals;

public class MyClassTest {

    MyClass tester = new MyClass();

    @Rule
    public final SystemOutRule systemOutRule = new SystemOutRule().enableLog();

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void testExceptionIsThrown() {
        tester.multiply(1000, 5);
    }

    @Test
    public void testMultiply() {
        assertEquals(50, tester.multiply(10, 5));
    }

    /*
    test to kill mutant
    */

    @Test
    public void kill999() {
        // PIT returneaza 56% fara si 60% cu acest test
        assertEquals(999, tester.multiply(999, 1));

        // PIT returneaza 60% fara si 64% cu acest test
        assertEquals("Produsul este calculat pt. x mai mic decat 1000\n",
                systemOutRule.getLogWithNormalizedLineSeparator());
    }

    @Test
    public void testAdd() {
        assertEquals(15,  tester.add(10, 5));
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
        assertEquals(4, tester.produsScalar(2,1,1,1,1,1));
        //assertEquals(-1, tester.produsScalar(2,1,1,0,-1,0));
        //assertEquals(1, tester.produsScalar(-1,-1,-1,-1,0,0));
    }

    @Test
    public void boundaryAnalysis() {
        assertEquals(3, tester.produsScalar(1,1,1,1,1,1));
        //assertEquals(0, tester.produsScalar(1,1,1,0,0,0)); nu e necesar
        //assertEquals(0, tester.produsScalar(0,0,0,1,1,1));
        //assertEquals(0, tester.produsScalar(0,0,0,0,0,0));
    }

    @Test
    public void categoryPartitioning() {
        assertEquals(4, tester.produsScalar(2,1,1,1,1,1));
        //assertEquals(-1, tester.produsScalar(2,1,1,0,-1,0));
        //assertEquals(1, tester.produsScalar(-1,-1,-1,-1,0,0));
        assertEquals(3, tester.produsScalar(1,1,1,1,1,1));
        //assertEquals(0, tester.produsScalar(1,1,1,0,0,0));
        //assertEquals(0, tester.produsScalar(0,0,0,0,0,0));
    }

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void testExceptionIsThrown2() {
        tester.produsScalar(2,1,1,0,-1,0);
        tester.produsScalar(-1,-1,-1,-1,0,0);
        tester.produsScalar(0,0,0,1,1,1);
        //tester.produsScalar(1,1,1,0,0,0);
        tester.produsScalar(0,0,0,0,0,0);
    }

    /*
    test to kill mutant
    */
    @org.junit.Test(expected = IllegalArgumentException.class)
    public void killX1() {
        // PIT returneaza 64% fara si 68% cu acest test
        tester.produsScalar(0,1,1,1,1,1);
    }

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void killX2() {
        // PIT returneaza 68% fara si 72% cu acest test
        tester.produsScalar(1,0,1,1,1,1);
    }

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void killX3() {
        tester.produsScalar(1,1,0,1,1,1);
    }

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void killY1() {
        tester.produsScalar(1,1,1,0,1,1);
    }

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void killY2() {
        tester.produsScalar(1,1,1,1,0,1);
    }

    @org.junit.Test(expected = IllegalArgumentException.class)
    public void killY3() {
        //PIT returneaza 88% cu acest test
        tester.produsScalar(1,1,1,1,1,0);
    }

    @Test
    public void killDiv() {
        //PIT returneaza 88% fara si 100% cu acest test
        assertEquals(12,tester.produsScalar(2,2,2,2,2,2));
    }
}