import java.awt.*;

public class Kreska{
    protected Point poczatek, koniec;
    protected Color kolor;
    public Kreska(Point pocz, Point kon, Color kol){
        if (pocz == null || kon == null || kol == null) {
            throw new IllegalArgumentException("Arguments cannot be null");
        }
        this.poczatek = pocz;
        this.koniec = kon;
        this.kolor = kol;
    }
}