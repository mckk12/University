public class WyrazeniaTest {
    void Wypisz_wyrazenie(Wyrazenie w){
        System.out.println("Wyrażenie: " + w);
        System.out.println("Wartość: " + w.oblicz());
        System.out.println();
    }

    void Test1(){
        Wyrazenie w = new Odejm(
        new Dodaj(
            new Liczba(7),
            new Mnoz(
                new Liczba(5),
                new Stala("x", 1.618)
                )
        ),
        Liczba.JEDEN
        );

        Wypisz_wyrazenie(w);
    }

    void Test2(){
        Wyrazenie w = new Mnoz(
            new Przec(new Odejm(
                new Liczba(2), 
                new Stala("x", 1.618))),
            Stala.E);

        Wypisz_wyrazenie(w);
    }

    void Test3(){
        Wyrazenie w = new Dziel(
            new Odejm(
                new Mnoz(
                    new Liczba(3),
                    Stala.Pi),
                Liczba.JEDEN),
             new Dodaj(
                new Odwr(new Stala("x", 1.618)),
                new Liczba(4)
             ));

        Wypisz_wyrazenie(w);
    }

    void Test4(){
        Wyrazenie w = new Sin(new Dziel(
            new Mnoz(
                new Dodaj(
                    new Stala("x", 1.618),
                    new Liczba(13)),
                Stala.Pi),
            new Odejm(
                Liczba.JEDEN, 
                new Stala("x", 1.618))
                ));

        Wypisz_wyrazenie(w);
    }

    void Test5(){
        Wyrazenie w = new Dodaj(
            new Exp(new Liczba(5)),
            new Mnoz(
                new Stala("x", 1.618),
                new Log(
                    Stala.E, 
                    new Stala("x", 1.618))
            ));

        Wypisz_wyrazenie(w);
    }
    public static void main(String[] args) {
        new WyrazeniaTest().Test1();
        new WyrazeniaTest().Test2();
        new WyrazeniaTest().Test3();
        new WyrazeniaTest().Test4();
        new WyrazeniaTest().Test5();
    };
}
