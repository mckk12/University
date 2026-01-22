import java.util.function.UnaryOperator;

public class CollatzProblem {
    static UnaryOperator<Integer> collatzLength = n -> {
        int length = 0;
        long current = n;
        while (current != 1) {
            if (current % 2 == 0) {
                current = current / 2;
            } else {
                current = 3 * current + 1;
            }
            length++;
        }
        return length + 1;
    };

    public static void main(String[] args) {
        int cZero = 27;
        int length = collatzLength.apply(cZero);
        System.out.println("Collatz sequence length for " + cZero + " is: " + length);

        cZero = 15;
        length = collatzLength.apply(cZero);
        System.out.println("Collatz sequence length for " + cZero + " is: " + length);

        cZero = 11;
        length = collatzLength.apply(cZero);
        System.out.println("Collatz sequence length for " + cZero + " is: " + length);

        cZero=1;
        length = collatzLength.apply(cZero);
        System.out.println("Collatz sequence length for " + cZero + " is: " + length);

    }
}
