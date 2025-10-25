package figury;

public final class Prosta {
    public final double a;
    public final double b;
    public final double c;

    public Prosta(double a, double b, double c) {
        if (a == 0 && b == 0) {
            throw new IllegalArgumentException("Współczynniki a i b nie mogą być jednocześnie zerowe.");
        }
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public static Prosta przesun(Prosta p, Wektor v) {
        return new Prosta(p.a, p.b, p.c - p.a * v.dx - p.b * v.dy);
    }

    public static boolean czyRownolegle(Prosta p1, Prosta p2) {
        return p1.a * p2.b == p2.a * p1.b;
    }

    public static boolean czyProstopadle(Prosta p1, Prosta p2) {
        return p1.a * p2.a + p1.b * p2.b == 0;
    }

    public static Punkt punktPrzeciecia(Prosta p1, Prosta p2) {
        if (czyRownolegle(p1, p2)) {
            throw new IllegalArgumentException("Proste są równoległe i nie mają punktu przecięcia.");
        }
        double det = p1.a * p2.b - p2.a * p1.b;
        double x = (p2.b * (-p1.c) - p1.b * (-p2.c)) / det;
        double y = (p1.a * (-p2.c) - p2.a * (-p1.c)) / det;
        return new Punkt(x, y);
    }
}
