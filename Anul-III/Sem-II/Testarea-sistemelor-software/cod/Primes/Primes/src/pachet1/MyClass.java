package pachet1;

import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;
import static java.lang.Math.sqrt;

public class MyClass {

    public static boolean isPrime(int n) {
        return n == 2
                || !(n < 2 || n % 2 == 0) &&
                !IntStream.rangeClosed(3, (int)sqrt(n))
                        .filter(x -> x % 2 != 0)
                        .anyMatch(x -> n % x == 0);
    }

    public static boolean solve(int n, int[] a, int i) {

        if ( n < 1 || n > 50 || i < 1 || i > n ) {
            System.out.println("Conditions not met!");
            return false;
        }

        if (Arrays.stream(a).anyMatch(x -> x < 0)) {
            System.out.println("Conditions not met!");
            return false;
        }

        return Arrays.stream(a).filter(x -> isPrime(x)).count() >= i;

    }

    /*
    public static void main(String[] args) {

        int n;
        int i;
        int[] a = null;
        try (Scanner sc = new Scanner(System.in)) {
            n = sc.nextInt();
            i = sc.nextInt();
            if(n > 0) {
            	a = new int[n];
            }

            for(int j = 0; j < n; j++) {
                a[j] = sc.nextInt();
            }
        }

        System.out.println(solve(a, n, i));

    }
    */

}
