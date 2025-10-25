package figury;

public class Odcinek {
    public Punkt a;
    public Punkt b;

    public Odcinek(Punkt a, Punkt b) {
        if (a == null || b == null) {
            throw new IllegalArgumentException("Punkty nie mogą być null.");
        }
        if (a.x == b.x && a.y == b.y) {
            throw new IllegalArgumentException("Punkty odcinka muszą być różne.");
        }
        this.a = a;
        this.b = b;
    }

    public void przesun(Wektor v) {
        a.przesun(v);
        b.przesun(v);
    }

    public void obroc(Punkt p, double kat) {
        a.obroc(p, kat);
        b.obroc(p, kat);
    }

    public void odbij(Prosta p) {
        a.odbij(p);
        b.odbij(p);
    }

    @Override
    public String toString() {
        return "Odcinek(" + a + ", " + b + ")";
    }
}
