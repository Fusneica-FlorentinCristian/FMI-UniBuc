/*
Graful partial asociat programului poate fi vizualizat prin intermediul site-ului:
https://app.code2flow.com
In folderul Materiale exista CFG_exemplu_curs.png

Despre plugin-ul de generare a mutantilor in Java, dar si despre
libraria SystemOutRule mai multe detalii in fisierul pluginuri_utile_Java.
*/

package pachet2;
import pachet1.*;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static pachet1.MyClass.main;

public class MyClassTest {

    MyClass tester = new MyClass();

    @Test
    public void equivalencePartitioning() {
        main(new String[]{"0", null, null, null});
        main(new String[]{"25", null, null, null});
        main(new String[]{"3", "a", "b", "c", "a", "y"});
        main(new String[]{"3", "a", "b", "c", "a", "n"});
        main(new String[]{"3", "a", "b", "c", "d", "y"});
        main(new String[]{"3", "a", "b", "c", "d", "n"});
    }

    @Test
    public void boundaryValueAnalysis() {
        main(new String[]{"0", null, null, null});
        main(new String[]{"21", null, null, null});
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "a", "n"});
        main(new String[]{"1", "a", "b", "y"});
        main(new String[]{"1", "a", "b", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "a", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "a", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "u", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "u", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "z", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "z", "n"});
    }

    @Test
    public void categoryPartitioning() {
        main(new String[]{"-5", null, null, null});
        main(new String[]{"0", null, null, null});
        main(new String[]{"21", null, null, null});
        main(new String[]{"25", null, null, null});
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "a", "n"});
        main(new String[]{"1", "a", "b", "y"});
        main(new String[]{"1", "a", "b", "n"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "a", "y"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "a", "n"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "c", "y"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "c", "n"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "e", "y"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "e", "n"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "f", "y"});
        main(new String[]{"5", "a", "b", "c", "d", "e", "f", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "a", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "a", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "c", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "c", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "u", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "u", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "z", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "z", "n"});
    }

    @Test
    public void statementCoverage(){
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "b", "n"});
    }

    @Test
    public void branchCoverage() {
        main(new String[]{"25", null, null, null});
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "b", "n"});

    }

    @Test
    public void conditionCoverage() {
        main(new String[]{"0", null, null, null});
        main(new String[]{"25", null, null, null});
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "b", "y"});

    }

    @Test
    public void pathCoverage() {
        main(new String[]{"-5", null, null, null});
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "a", "n"});
        main(new String[]{"1", "a", "b", "y"});
        main(new String[]{"1", "a", "b", "n"});

    }

    // Mutation coverage before and after run all tests including killMutants 47% sau 15/32
    @Test
    public void killMutants() {
        main(new String[]{"1", "a", "a", "y"});
        main(new String[]{"1", "a", "a", "n"});
        main(new String[]{"1", "a", "b", "y"});
        main(new String[]{"1", "a", "b", "n"});

        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "a", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "a", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "c", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "c", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "u", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "u", "n"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "z", "y"});
        main(new String[]{"20", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "z", "n"});

    }
}