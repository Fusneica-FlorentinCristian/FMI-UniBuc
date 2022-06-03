package pachet2;
import pachet1.MyClass;
import org.junit.Test;
/**
 * Created by sorinapredut on 25/02/2019.
 */
public class MyClassTest {
    MyClass tester = new MyClass();

    // infinite loop
    // a se vedea rezolvari echivalente: Proiect, respectiv Proiect_v2
    @Test
    public void testMain() {
        tester.main(new String[]{"0", "", "", "n"});
        //tester.main(new String[]{"3", "a", "b", "c", "d", "n"});

    }
    /*
    @Test
    public void equivalencePartitioning() {

        tester.main(new String[]{"0", "", "", "y"});
        tester.main(new String[]{"0", null, null, "y"});
        tester.main(new String[]{"3", "a", "b", "c", "a", "y"});
        tester.main(new String[]{"3", "a", "b", "c", "a", "n"});
        tester.main(new String[]{"3", "a", "b", "c", "d", "y"});
        tester.main(new String[]{"3", "a", "b", "c", "d", "n"});
    }

    @Test
    public void boundaryValueAnalysis() {

    }

    @Test
    public void categoryPartitioning() {

    }

    @Test
    public void statementCoverage() {

    }

    @Test
    public void branchCoverage() {

    }

    @Test
    public void conditionCoverage() {

    }

    @Test
    public void circuitCoverage() {

    }

    @Test
    public void pathCoverage() {

    }

    @Test
    public void killMutants() {

    }
    */
}
