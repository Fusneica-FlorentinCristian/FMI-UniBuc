package pachet2;

import org.junit.Before;
import org.junit.Test;
import static pachet1.MyClass.solve;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import java.util.Random;
import java.util.stream.IntStream;

public class MyClassTest {

    Random r;

    public void PrimesTest() {
        r = new Random(System.nanoTime());
    }

    @Before
    public void setUp() {
        r = new Random(System.nanoTime());
    }

    public int [] nullOrArr() {
        return r.nextInt(2) == 0 ? null : new int [1];
    }

    @Test
    public void equivalencePartitioning() {
        assertTrue( solve( 4, new int [] {2, 3, 4, 5}, 3) );
        assertFalse( solve( 4, new int [] {2, 3, 4, 5}, 4) );
        assertFalse( solve( 4, new int [] {2, 3, 4, 5}, -3) );
        assertFalse( solve( 4, new int [] {2, 3, 4, 5}, 5) );
        assertFalse( solve( 4, new int [] {-2, 3, 4, 5}, 1 ) );
        assertFalse( solve( 0, nullOrArr(), r.nextInt() ) );
        assertFalse( solve( 51, nullOrArr(), r.nextInt() ) );
    }

    @Test
    public void boundaryValueAnalysis() {
        assertTrue( solve( 4, new int [] {3}, 1) );
        assertTrue( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = 3).toArray(), 1) );
        assertFalse( solve( 1, new int [] {2}, 50) );
        assertTrue( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = 2).toArray(), 50) );
        assertFalse( solve( 0, nullOrArr(), 1 ) );
        assertFalse( solve( 0, nullOrArr(), 0 ) );
        assertFalse( solve( 51, IntStream.rangeClosed(1, 51).map(x-> x = 2).toArray(), 1 ) );
        assertFalse( solve( 51, IntStream.rangeClosed(1, 51).map(x-> x = 2).toArray(), 51 ) );
    }

    @Test
    public void categoryPartitioning() {
        assertFalse( solve( -1, nullOrArr(), r.nextInt()) );
        assertFalse( solve( -1, new int[]{}, r.nextInt()) );
        assertTrue( solve( 1, new int [] {2}, 1) );
        assertFalse( solve( 1, new int [] {2}, 0) );
        assertFalse( solve( 1, new int [] {2}, 5) );
        assertFalse( solve( 1, new int [] {-1}, 1) );
        assertTrue( solve( 2, new int [] {2, 3}, 2) );
        assertFalse( solve( 2, new int [] {2, 2}, 0) );
        assertFalse( solve( 2, new int [] {2, 2}, 3) );
        assertFalse( solve( 2, new int [] {3, -14}, 1) );
        assertTrue( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = 2).toArray(), 4) );
        assertFalse( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = 2).toArray(), 0) );
        assertFalse( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = 2).toArray(), 51) );
        assertFalse( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = -2).toArray(), 4) );
        assertFalse( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x = -2).toArray(), 4) );
        assertFalse( solve( 51, nullOrArr(), r.nextInt()) );


    }

    @Test
    public void statementCoverage() {
        assertFalse( solve( 0, nullOrArr(), r.nextInt()) );
        assertFalse( solve( 1, new int[]{-4}, r.nextInt()) );
        assertTrue( solve( 1, new int[]{2}, 1) );
    }

    @Test
    public void branchCoverage() {
        assertFalse( solve( 0, nullOrArr(), r.nextInt()) );
        assertFalse( solve( 1, new int[]{9}, 1) );
        assertFalse( solve( 1, new int[]{-9}, 1) );
        assertTrue( solve( 1, new int[]{7}, 1) );
    }

    @Test
    public void conditionCoverage() {
        assertFalse( solve( 0, nullOrArr(), r.nextInt()) );
        assertFalse( solve( 51, IntStream.rangeClosed(1, 51).map(x-> x = 2).toArray(), r.nextInt()) );
        assertFalse( solve( 1, new int[]{2}, 0) );
        assertFalse( solve( 1, new int[]{2}, 2) );
        assertFalse( solve( 1, new int[]{-1}, 1) );
        assertTrue( solve( 1, new int[]{2}, 1) );

    }

    @Test
    public void pathCoverage() {
        assertFalse( solve( 0, nullOrArr(), r.nextInt()) );
        assertFalse( solve( 1, new int[]{-1}, r.nextInt()) );
        assertTrue( solve( 1, new int[]{2}, 1) );
    }

    @Test
    public void killChangedConditionalBoundary() {
        assertTrue( solve( 50, IntStream.rangeClosed(1, 50).map(x-> x != 2 ? 0 : x ).toArray(), 1) );
    }

}
