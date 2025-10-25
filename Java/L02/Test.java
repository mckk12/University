import figury.*;

public class Test {
    public static void main(String[] args) {
        // Test Punkt
        Punkt p1 = new Punkt(1, 2);
        Punkt p2 = new Punkt(3, 4);
        Wektor v = new Wektor(2, -1);
        Prosta prosta1 = new Prosta(1, -1, 0); // x - y = 0
        Prosta prosta2 = new Prosta(0, 1, -2); // y = 2

        System.out.println("Punkt przed przesunięciem: " + p1);
        p1.przesun(v);
        System.out.println("Punkt po przesunięciu: " + p1);

        p1.obroc(p2, Math.PI / 2);
        System.out.println("Punkt po obrocie o 90 stopni wokół (3,4): " + p1);

        p1.odbij(prosta1);
        System.out.println("Punkt po odbiciu względem prostej x-y=0: " + p1);

        // Test Odcinek
        Odcinek odc = new Odcinek(new Punkt(0, 0), new Punkt(2, 0));
        System.out.println("\nOdcinek przed przesunięciem: " + odc);
        odc.przesun(v);
        System.out.println("Odcinek po przesunięciu: " + odc);

        odc.obroc(p2, Math.PI / 4);
        System.out.println("Odcinek po obrocie o 45 stopni wokół (3,4): " + odc);

        odc.odbij(prosta2);
        System.out.println("Odcinek po odbiciu względem prostej y=2: " + odc);

        // Test Trojkat
        Trojkat t = new Trojkat(new Punkt(0, 0), new Punkt(1, 0), new Punkt(0, 1));
        System.out.println("\nTrojkat przed przesunięciem: " + t);
        t.przesun(v);
        System.out.println("Trojkat po przesunięciu: " + t);

        t.obroc(p2, Math.PI);
        System.out.println("Trojkat po obrocie o 180 stopni wokół (3,4): " + t);

        t.odbij(prosta1);
        System.out.println("Trojkat po odbiciu względem prostej x-y=0: " + t);

        // Test Wektor
        Wektor v2 = new Wektor(-1, 3);
        Wektor vSum = Wektor.zloz(v, v2);
        System.out.println("\nSuma wektorów: " + vSum.dx + ", " + vSum.dy);

        // Test Prosta
        Prosta przesunieta = Prosta.przesun(prosta1, v);
        System.out.println("Prosta po przesunięciu o wektor (2,-1): " +
            przesunieta.a + "x + " + przesunieta.b + "y + " + przesunieta.c + " = 0");

        boolean rownolegle = Prosta.czyRownolegle(prosta1, prosta2);
        boolean prostopadle = Prosta.czyProstopadle(prosta1, prosta2);
        System.out.println("Czy proste są równoległe? " + rownolegle);
        System.out.println("Czy proste są prostopadłe? " + prostopadle);

        try {
            Punkt przeciecie = Prosta.punktPrzeciecia(prosta1, prosta2);
            System.out.println("Punkt przecięcia prostych: " + przeciecie);
        } catch (IllegalArgumentException e) {
            System.out.println("Proste są równoległe, brak punktu przecięcia.");
        }
    }
}
