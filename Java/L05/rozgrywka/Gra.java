package rozgrywka;
import obliczenia.Wymierna;

/**
 * Reprezentuje stan pojedynczej gry losowania ułamka a/b ∈ (0,1).
 */

public class Gra {
    private int zakres;
    private Wymierna liczba;
    private int maksIloscProb;
    private int licznikProb;

    private boolean gameState;
    private int finishState; //0 - rezygnacja, 1 - porażka, 2 - wygrana

    public Wymierna getAnswer() {
        return liczba;
    }

    public boolean isActive() {
        return gameState;
    }

    public int getFinishState() {
        return finishState;
    }

    public int getProba() {
        return licznikProb;
    }

    public int getMaksProb() {
        return maksIloscProb;
    }

    /**
     * Rozpoczyna grę z parametrem z (zakres).
     * Na końcu dodano asercję sprawdzającą, że licznik < mianownik.
     *
     * @param z zakres losowanych wartości (mianownik i licznik z przedziału 1..z)
     */
    public void start(int z){
        if (z < 5 || z > 20) {
            throw new IllegalArgumentException("Zakres musi byc w przedziale <5,20>.");
        }
        this.zakres = z;
        int licz = (int)(Math.random() * zakres) + 1;
        int mian = (int)(Math.random() * zakres) + 1;
        this.liczba = new Wymierna(licz, mian);
        this.maksIloscProb = (int) Math.ceil(3.0 * Math.log(z));
        this.licznikProb = 0;
        assert this.liczba.getLicznik() < this.liczba.getMianownik() : "Licznik powinien być mniejszy od mianownika";
        this.gameState = true;
        this.finishState = -1; //gra w toku
    }

    /** 
     * Metoda przyjmująca próbę odgadnięcia liczby.
     * Zwraca true, jeśli próba jest poprawna, w przeciwnym razie false.
     * Rzuca wyjątek IllegalStateException, jeśli liczba prób przekroczyła maksymalną dozwoloną ilość.
     * Zmienia stan rozgrywki w przypadku wygranej lub przegranej.
     *
     * @param proba próba odgadnięcia liczby
     * @return true jeśli próba jest poprawna, false w przeciwnym razie
     * @throws IllegalStateException jeśli liczba prób przekroczyła maksymalną dozwoloną ilość
     */
    public int zgadnij(Wymierna proba) {
        if (licznikProb >= maksIloscProb) {
            throw new IllegalStateException("Przekroczono maksymalna ilosc prob.");
        }
        licznikProb++;
        int res = proba.compareTo(liczba);
        if(res==0){
            finishState = 2; //wygrana
            gameState = false;
            return 0;
        }
        if(licznikProb >= maksIloscProb){
            finishState = 1; //porażka
            gameState = false;
        }

        return res;

    }



    public void rezygnuj() {
        finishState = 0; //rezygnacja
        gameState = false;
    }

}
