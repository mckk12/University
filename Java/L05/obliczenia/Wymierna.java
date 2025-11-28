package obliczenia;

/**
 * Reprezentacja liczby wymiernej jako nieskracalnego ułamka.
 * Licznik i mianownik przechowywane są jako int; znak przesunięty jest zawsze do licznika,
 * a mianownik jest dodatni (>0).
 */
public class Wymierna implements Comparable<Wymierna> {
    private int licznik, mianownik = 1;

    // konstruktor bezparametrowy tworzy 0/1
    public Wymierna() {
        this(0, 1);
    }

    // konstruktor jednoargumentowy tworzy k/1
    public Wymierna(int k) {
        this(k, 1);
    }

    // konstruktor dwuargumentowy tworzy k/m
    public Wymierna(int k, int m) {
        if (m == 0) {
            throw new IllegalArgumentException("Mianownik nie moze byc zerem.");
        }
        if (m < 0) {
            k = -k;
            m = -m;
        }
        int nwd = nwd(Math.abs(k), m);
        if (nwd != 0) {
            k /= nwd;
            m /= nwd;
        }
        this.licznik = k;
        this.mianownik = m;

    }

    //rekurencyjna funkcja obliczajaca NWD
    private int nwd(int a, int b) {
        if (b==0) return a;
        return nwd(b, a % b);
    }
        

    public int getLicznik() {
        return licznik;
    }

    public int getMianownik() {
        return mianownik;
    }

    @Override
    public String toString() {
        return licznik + "/" + mianownik;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Wymierna wymierna = (Wymierna) obj;
        return licznik == wymierna.licznik && mianownik == wymierna.mianownik;
    }

    @Override
    public int compareTo(Wymierna other) {
        return Integer.compare(this.licznik * other.mianownik, other.licznik * this.mianownik);
    }

    // operacje statyczne
    public static Wymierna dodaj(Wymierna a, Wymierna b) {
        return new Wymierna(a.licznik * b.mianownik + b.licznik * a.mianownik, a.mianownik * b.mianownik);
    }
    public static Wymierna odejmij(Wymierna a, Wymierna b) {
        return new Wymierna(a.licznik * b.mianownik - b.licznik * a.mianownik, a.mianownik * b.mianownik);
    }
    public static Wymierna mnoz(Wymierna a, Wymierna b) {
        return new Wymierna(a.licznik * b.licznik, a.mianownik * b.mianownik);
    }
    public static Wymierna dziel(Wymierna a, Wymierna b) {
        if (b.licznik == 0) {
            throw new ArithmeticException("Nie mozna dzielic przez zero.");
        }
        return new Wymierna(a.licznik * b.mianownik, a.mianownik * b.licznik);
    }
}