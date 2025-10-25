package figury;

public class Trojkat {
    public Punkt p1;
    public Punkt p2;
    public Punkt p3;

    public Trojkat(Punkt p1, Punkt p2, Punkt p3) {
        if (p1 == null || p2 == null || p3 == null) {
            throw new IllegalArgumentException("Punkty nie mogą być null.");
        }
        if (p1.x == p2.x && p1.y == p2.y ||
            p1.x == p3.x && p1.y == p3.y ||
            p2.x == p3.x && p2.y == p3.y) {
            throw new IllegalArgumentException("Punkty trójkąta muszą być różne.");
        }
        if((p2.x - p1.x) * (p3.y - p1.y) == (p3.x - p1.x) * (p2.y - p1.y)) {
            throw new IllegalArgumentException("Punkty trójkąta nie mogą być współliniowe.");
        }
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;

    }

    public void przesun(Wektor v) {
        p1.przesun(v);
        p2.przesun(v);
        p3.przesun(v);
    }

    public void obroc(Punkt p, double kat) {
        p1.obroc(p, kat);
        p2.obroc(p, kat);
        p3.obroc(p, kat);
    }

    public void odbij(Prosta p) {
        p1.odbij(p);
        p2.odbij(p);
        p3.odbij(p);
    }

    @Override
    public String toString() {
        return "Trojkat(" + p1 + ", " + p2 + ", " + p3 + ")";
    }
}
