package pachet1;

public class MyClass {
    public void find(int n, String x, char c, char s) {
        int i;
        boolean found = false;
        if (n<1 || n>20) {
            System.out.println("Input integer between 1 and 20.\n");
            return;
        }
        for(i=0; !found && i<n; i++)
            if(x.charAt(i) == c)
                found = true;
        if(found)
            System.out.println("Character "+ c +" appears at position " + i + ".");
        else
            System.out.println("Character "+ c +" does not appear in the string.");
        if (Character.toLowerCase(s) == 'y')
            System.out.println("Input character to search for.");
        System.out.println();
    }
}