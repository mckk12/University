interface Obliczalny {
      double oblicz();
}

abstract class Wyrazenie implements Obliczalny {
      public static double suma(Wyrazenie... wyr) {
            double suma = 0;
            for (Wyrazenie w : wyr) {
                  suma += w.oblicz();
            }
            return suma;
      }

      public static double iloczyn(Wyrazenie... wyr) {
            double iloczyn = 1;
            for (Wyrazenie w : wyr) {
                  iloczyn *= w.oblicz();
            }
            return iloczyn;
      }
}

class Liczba extends Wyrazenie {
      double wartosc;
      public static final Liczba ZERO = new Liczba(0.0);
      public static final Liczba JEDEN = new Liczba(1.0);

      public Liczba(double wartosc) {
            this.wartosc = wartosc;
      }

      public double oblicz() {
            return wartosc;
      }

      @Override
      public String toString() {
            return Double.toString(wartosc);
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Liczba l) && Double.compare(l.wartosc, wartosc) == 0;
      }
}

class Stala extends Wyrazenie {
      String nazwa;
      double wartosc;
      public final static Stala Pi = new Stala("Pi", 3.14);
      public final static Stala E = new Stala("e", 2.72);

      public Stala(String nazwa, double wartosc) {
            this.nazwa = nazwa;
            this.wartosc = wartosc;
      }

      public double oblicz() {
            return wartosc;
      }

      @Override
      public String toString() {
            return nazwa;
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Stala s) && s.nazwa.equals(nazwa);
      }
}

class Przec extends Wyrazenie {
      final Wyrazenie arg;
      public Przec(Wyrazenie arg) {
            this.arg = arg;
      }

      public double oblicz() {
            return -arg.oblicz();
      }

      @Override
      public String toString() {
            return "~ " + arg.toString();
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Przec p) && p.arg.equals(arg);
      }
}

class Odwr extends Wyrazenie {
      final Wyrazenie arg;
      public Odwr(Wyrazenie arg) {
            this.arg = arg;
      }

      public double oblicz() {
            return 1.0 / arg.oblicz();
      }

      @Override
      public String toString() {
            return "! " + arg.toString();
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Odwr o) && o.arg.equals(arg);
      }
}

class Dodaj extends Wyrazenie {
      final Wyrazenie arg1;
      final Wyrazenie arg2;
      public Dodaj(Wyrazenie arg1, Wyrazenie arg2) {
            this.arg1 = arg1;
            this.arg2 = arg2;
      }

      public double oblicz() {
            return arg1.oblicz() + arg2.oblicz();
      }

      @Override
      public String toString() {
            return "(" + arg1.toString() + " + " + arg2.toString() + ")";
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Dodaj d) && d.arg1.equals(arg1) && d.arg2.equals(arg2);
      }
}

class Odejm extends Wyrazenie {
      final Wyrazenie arg1;
      final Wyrazenie arg2;
      public Odejm(Wyrazenie arg1, Wyrazenie arg2) {
            this.arg1 = arg1;
            this.arg2 = arg2;
      }

      public double oblicz() {
            return arg1.oblicz() - arg2.oblicz();
      }

      @Override
      public String toString() {
            return "(" + arg1.toString() + " - " + arg2.toString() + ")";
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Odejm o) && o.arg1.equals(arg1) && o.arg2.equals(arg2);
      }
}

class Mnoz extends Wyrazenie {
      final Wyrazenie arg1;
      final Wyrazenie arg2;
      public Mnoz(Wyrazenie arg1, Wyrazenie arg2) {
            this.arg1 = arg1;
            this.arg2 = arg2;
      }

      public double oblicz() {
            return arg1.oblicz() * arg2.oblicz();
      }

      @Override
      public String toString() {
            return arg1.toString() + " * " + arg2.toString();
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Mnoz m) && m.arg1.equals(arg1) && m.arg2.equals(arg2);
      }
}

class Dziel extends Wyrazenie {
      final Wyrazenie arg1;
      final Wyrazenie arg2;
      public Dziel(Wyrazenie arg1, Wyrazenie arg2) {
            this.arg1 = arg1;
            this.arg2 = arg2;
      }

      public double oblicz() {
            return arg1.oblicz() / arg2.oblicz();
      }

      @Override
      public String toString() {
            return arg1.toString() + " / " + arg2.toString();
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Dziel d) && d.arg1.equals(arg1) && d.arg2.equals(arg2);
      }
}

class Ln extends Wyrazenie {
      final Wyrazenie arg;
      public Ln(Wyrazenie arg) {
            this.arg = arg;
      }

      public double oblicz() {
            return Math.log(arg.oblicz());
      }

      @Override
      public String toString() {
            return "ln(" + arg.toString() + ")";
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Ln l) && l.arg.equals(arg);
      }
}

class Exp extends Wyrazenie {
      final Wyrazenie arg;
      public Exp(Wyrazenie arg) {
            this.arg = arg;
      }

      public double oblicz() {
            return Math.exp(arg.oblicz());
      }

      @Override
      public String toString() {
            return "exp(" + arg.toString() + ")";
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Exp e) && e.arg.equals(arg);
      }
}

class Sin extends Wyrazenie {
      final Wyrazenie arg;
      public Sin(Wyrazenie arg) {
            this.arg = arg;
      }

      public double oblicz() {
            return Math.sin(arg.oblicz());
      }

      @Override
      public String toString() {
            return "sin(" + arg.toString() + ")";
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Sin s) && s.arg.equals(arg);
      }
}

class Cos extends Wyrazenie {
      final Wyrazenie arg;
      public Cos(Wyrazenie arg) {
            this.arg = arg;
      }

      public double oblicz() {
            return Math.cos(arg.oblicz());
      }

      @Override
      public String toString() {
            return "cos(" + arg.toString() + ")";
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Cos c) && c.arg.equals(arg);
      }
}

class Log extends Wyrazenie {
      Wyrazenie podstawa;
      Wyrazenie arg;
      public Log(Wyrazenie podstawa, Wyrazenie arg) {
            this.podstawa = podstawa;
            this.arg = arg;
      }
      public double oblicz() {
            return Math.log(arg.oblicz()) / Math.log(podstawa.oblicz());
      }
      @Override
      public String toString() {
            return "log(" + podstawa.toString() + ", " + arg.toString() + ")";
      }
      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Log l) && l.podstawa.equals(podstawa) && l.arg.equals(arg);
      }
}

class Pot extends Wyrazenie {
      final Wyrazenie podstawa;
      final Wyrazenie wykladnik;
      public Pot(Wyrazenie podstawa, Wyrazenie wykladnik) {
            this.podstawa = podstawa;
            this.wykladnik = wykladnik;
      }

      public double oblicz() {
            return Math.pow(podstawa.oblicz(), wykladnik.oblicz());
      }

      @Override
      public String toString() {
            return podstawa.toString() + "^" + wykladnik.toString();
      }

      @Override
      public boolean equals(Object obj) {
            return (obj instanceof Pot p) && p.podstawa.equals(podstawa) && p.wykladnik.equals(wykladnik);
      }
}