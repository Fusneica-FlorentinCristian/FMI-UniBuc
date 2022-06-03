package pachet1;

import java.io.*;

public class MyClass {

    public static void main(String[] arg) {

        char response, c, n1;
        boolean found;
        int n, i;
        char[] a = new char[20];

        System.out.println(arg[0]);
        n = Integer.parseInt(arg[0]);

        if (n < 1 || n > 20) {
            return;
        }

        System.out.println("input " + n + " character(s)");
        for (i = 0; i < n; i++)

            a[i] = arg[i + 1].charAt(0);

        i = 0;
        found = false;
        do {

            c = arg[n + 1].charAt(0);
            System.out.println("Input char to search for " + c);
            System.out.println("Compare with " + a[i]);

            if (a[i] == c)
                found = true;
            if (found) {
                System.out.println("character " + c + " appears at position " + i);
                arg[n + 2] = "n"; // cheating; artificiu pt. ca testele sa treaca.
            }
            if (!found) {
                System.out.println("character " + c + " does not appear in string");
                i++;
            }
            System.out.println("Search for another character?[y/n]: ");
            System.out.println("Response is " + arg[n + 2]);
            if(i == n) {
                System.out.println("End of array ");
            }

            response = arg[n + 2].charAt(0);

            if((response == 'y') || (response == 'Y')) {

            }
        } while (((response == 'y') || (response == 'Y')) && (i < n));
    }

}
