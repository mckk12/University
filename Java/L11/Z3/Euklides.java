import java.util.function.BinaryOperator;

public class Euklides {
    static BinaryOperator<Integer> nwd = (a, b) -> {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    public static void main(String[] args) {
        int a = 48;
        int b = 18;
        int result = nwd.apply(a, b);
        System.out.println("NWD of " + a + " and " + b + " is: " + result);

        a = 56;
        b = 98;
        result = nwd.apply(a, b);
        System.out.println("NWD of " + a + " and " + b + " is: " + result);

        a = 101;
        b = 10;
        result = nwd.apply(a, b);
        System.out.println("NWD of " + a + " and " + b + " is: " + result);
    }
    
}
