package pachet1;
import java.util.Scanner;

/**
 * Created by sorinapredut on 5/03/2020.
 */

public class MyClass {
    public static void main(String[] arg) {

        //KeyboardInput in = new KeyboardInput();   //deprecated
        Scanner in = new Scanner(System.in);
        char response,c,n1;
        boolean found;
        int n,i;
        char[]a = new char[20];
        do {
            System.out.println("Input an integer between 1 and 20: ");
            //n = in.readInteger();   //deprecated
            n = in.nextInt();
            //System.out.println(arg[0]);   // using arg
            //n=Integer.parseInt(arg[0]);   // using arg
        } while (n<1 || n>20);
        System.out.println("input "+n+" character(s)");
        for(i=0;i<n;i++)
            //a[i] = in.readCharacter();   //deprecated
            a[i]=in.next(".").charAt(0);
        //a[i] = arg[i+1].charAt(0);   // using arg
        //n1 = in.readCharacter();   //deprecated
        n1 = in.next(".").charAt(0);
        do {
            System.out.println("Input character to search for: ");
            //c = in.readCharacter();   //deprecated
            c = in.next(".").charAt(0);
            //c = arg[n+1].charAt(0);   // using arg
            //n1 = in.readCharacter();   //deprecated
            n1 = in.next(".").charAt(0);
            found = false;
            for(i=0;!found && i<n;i++)
                if(a[i] == c)
                    found = true;
            if(found)
                System.out.println("character "+ c +" appears at position "+i);
            else
                System.out.println("character "+ c +" not appear in string");
            System.out.println("Search for another character?[y/n]: ");
            //response = in.readCharacter();   //deprecated
            response = in.next(".").charAt(0);
            //response = arg[n+2].charAt(0);   // using arg
            //n1 = in.readCharacter();   //deprecated
            n1 = in.next(".").charAt(0);
        } while((response == 'y')||(response == 'Y'));
    }
}