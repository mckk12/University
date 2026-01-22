import java.util.Arrays;

public class Trojkat implements Comparable<Trojkat> {
    double a;
    double b;
    double c;

    public Trojkat(double a, double b, double c) {
        validateSides(a, b, c);
        this.a = a;
        this.b = b;
        this.c = c;
    }

    private void validateSides(double a, double b, double c) {
        double[] sides = {a, b, c};
        Arrays.sort(sides);
        if (sides[0] + sides[1] <= sides[2]) {
            throw new IllegalArgumentException("Invalid triangle sides: " + a + ", " + b + ", " + c);
        }
    }

    private double getPerimeter() {
        return a + b + c;
    }

    @Override
    public int compareTo(Trojkat other) {
        return Double.compare(this.getPerimeter(), other.getPerimeter());
    }

    @Override
    public String toString() {
        return "Trojkat{" +"a=" + a +", b=" + b +", c=" + c + ", perimeter=" + getPerimeter() +'}';
    }
}