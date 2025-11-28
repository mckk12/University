import obliczenia.Wymierna;
import rozgrywka.Gra;
import java.util.Scanner;
import java.util.logging.Logger;


public class Zgadywanka {
    private static final Logger logger = Logger.getLogger(Zgadywanka.class.getName());

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String playerName;

        try (java.io.FileInputStream fis = new java.io.FileInputStream("logging.properties")) {
            java.util.logging.LogManager.getLogManager().readConfiguration(fis);
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

        System.out.println("Witaj w grze Zgadywanka liczby wymiernej (ułamka)!");
        System.out.println("Podaj swoje imie: ");
        playerName = scanner.nextLine();
        
        Gra gra = new Gra();
        
        while (true)
        {    
            System.out.println("\nOpcje: (n)owa gra, (q)uit");
            System.out.print("Wybierz: ");
            String option = scanner.nextLine().trim().toLowerCase();
            if (option.equals("q") || option.equals("quit")) {
                System.out.println("Do widzenia!");
                logger.info("Koniec programu. Gracz " + playerName + " opuścił aplikację.");
                break;
            } else if (option.equals("n") || option.equals("nowa") || option.equals("nowa gra")) {

                logger.info("Gracz " + playerName + " rozpoczyna nowa gre.");

                System.out.print("Podaj zakres gry (5-20): ");
                String z = scanner.nextLine().trim();
                int zakres;
                try {
                    zakres = Integer.parseInt(z);
                } catch (NumberFormatException e) {
                    System.out.println("Niepoprawna liczba.");
                    logger.warning("Niepoprawna liczba zakresu: " + z);
                    continue;
                }

                try {
                    gra.start(zakres);
                    logger.info("Gra rozpoczęta z zakresem: " + zakres + ". Szukana liczba to: " + gra.getAnswer());
                } catch (AssertionError ae) {
                    System.out.println("Blad generowanie gry: " + ae.getMessage());
                    logger.warning("Blad generowanie gry: " + ae.getMessage());
                    continue;
                } catch (IllegalArgumentException e) {
                    System.out.println("Błąd: " + e.getMessage());
                    logger.warning("Start gry nieudany: " + e.getMessage());
                    continue;
                }

                while (gra.isActive()){
                    System.out.printf("Pozostało %d prób. Podaj propozycję w formacie licznik/mianownik (np. 3/7), lub 'poddaj' aby się poddać: ",
                            gra.getMaksProb() - gra.getProba());

                    String line = scanner.nextLine().trim();
                    if (line.equalsIgnoreCase("poddaj")) {
                        gra.rezygnuj();
                        System.out.println("Poddajesz się. Koniec rundy.");
                        break;
                    }        

                    try {
                        Wymierna proba = parseWymierna(line, zakres);
                        logger.info("Gracz " + playerName + " proba nr " + (gra.getProba() + 1) + ": " + proba);
                        int res = gra.zgadnij(proba);
                        if (res < 0) {
                            System.out.println("Za mało.");
                        } else if (res > 0) {
                            System.out.println("Za dużo.");
                        } 
                        
                    } catch (GraException ge) {
                        System.out.println("Błąd: " + ge.getMessage());
                        logger.warning("Blad podczas proby odgadniecia liczby: " + ge.getMessage());
                    } catch (IllegalStateException ise) {
                        System.out.println("Koniec gry: " + ise.getMessage());
                        logger.info("Koniec gry dla gracza " + playerName + ": " + ise.getMessage());
                    }
                    
                }
            } else {
                System.out.println("Nieznana opcja. Sprobuj ponownie.");
                continue;
            }

            if (gra.getFinishState() == 2) {
                System.out.println("Gratulacje! Wygrales!");
                logger.info("Gracz " + playerName + " wygral rozgrywke.");
            } else if (gra.getFinishState() == 0) {
                System.out.println("Zrezygnowano. Szukana liczba to: " + gra.getAnswer());
                logger.info("Gracz " + playerName + " zrezygnowal z rozgrywki.");
            } else {
                System.out.println("Niestety, przegrales. Szukana liczba to: " + gra.getAnswer());
                logger.info("Gracz " + playerName + " przegral rozgrywke.");
            }

        }
        scanner.close();
    }

    private static Wymierna parseWymierna(String input, int zakres) throws GraException {
        String[] parts = input.split("/");
        if (parts.length != 2) {
            throw new InvalidFormatException("Niepoprawny format. Użyj licznik/mianownik.");
        }

        int licznik, mianownik;
        try {
            licznik = Integer.parseInt(parts[0].trim());
            mianownik = Integer.parseInt(parts[1].trim());
        } catch (NumberFormatException e) {
            throw new InvalidFormatException("Niepoprawny format. Licznik i mianownik muszą być liczbami całkowitymi.");
        }

        if (licznik > mianownik || (licznik < 0 && mianownik > 0) || (licznik > 0 && mianownik < 0)) {
            throw new ValueOutOfRangeException("Liczba powinna znajdować się w przedziale (0-1).");
        }

        if (mianownik > zakres) {
            throw new DenominatorTooLargeException("Mianownik nie może być większy niż podany zakres(" + zakres + ").");
        }

        return new Wymierna(licznik, mianownik);
    }
    
}
