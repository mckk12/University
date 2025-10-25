package figury;

public class Punkt {
     double x;
     double y;

    public double getX() {return x;}
    public double getY() {return y;}

    public Punkt(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public void przesun(Wektor v) {
        this.x += v.dx;
        this.y += v.dy;
    }

    public void obroc(Punkt p, double kat) {
        double newX = p.x + (x - p.x) * Math.cos(kat) - (y - p.y) * Math.sin(kat);
        double newY = p.y + (x - p.x) * Math.sin(kat) + (y - p.y) * Math.cos(kat);
        this.x = newX;
        this.y = newY;
    }

    public void odbij(Prosta p){
        double det = p.a*p.a + p.b*p.b;
        if (det == 0) {
            throw new IllegalArgumentException("Prosta nie może mieć współczynników a i b równych zero.");
        }
        double newX = ((p.b*p.b-p.a*p.a)*x - 2*p.a*p.b*y - 2*p.a*p.c)/det;
        double newY = ((p.a*p.a-p.b*p.b)*y - 2*p.a*p.b*x - 2*p.b*p.c)/det;
        this.x = newX;
        this.y = newY;
    }

    @Override
    public String toString() {
        return String.format("Punkt(%.2f, %.2f)", x, y);
    }
}
