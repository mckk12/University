package figury;

public final class Wektor {
    public final double dx;
    public final double dy;

    public Wektor(double dx, double dy) {
        this.dx = dx;
        this.dy = dy;
    }

    public static Wektor zloz(Wektor v1, Wektor v2) {
        return new Wektor(v1.dx + v2.dx, v1.dy + v2.dy);
    }
}
