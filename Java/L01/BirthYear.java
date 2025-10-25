import java.util.*;

public class BirthYear {

    // tablica z wybranymi liczbami rzymskimi
    private static String[] rzymskie = {"M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    // tablica z odpowiadającymi liczbom rzymskim wartościami
    private static int[] arabskie = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    public static String rzymska(int n){
        if (n <= 0 || n >= 4000) {
            throw new IllegalArgumentException("rok " + n + " spoza zakresu");
        }
        String romanNumber = "";
        for (int i = 0; i < arabskie.length; i++) {
            while (n >= arabskie[i]) {
                romanNumber += rzymskie[i];
                n -= arabskie[i];
            }
        }
        return romanNumber;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.err.print("Podaj swoje imię: ");
        String name = scanner.nextLine();

        System.err.print("Podaj rok urodzenia: ");
        int year = scanner.nextInt();
        scanner.close();

        String[] patrons = {
            "szczur", "bawół", "tygrys", "królik", "smok", "wąż",
            "koń", "owca", "małpa", "kogut", "pies", "świnia"
        };

        String patron;
        switch ((year + 8) % 12) {
            case 0 -> patron = patrons[0];
            case 1 -> patron = patrons[1];
            case 2 -> patron = patrons[2];
            case 3 -> patron = patrons[3];
            case 4 -> patron = patrons[4];
            case 5 -> patron = patrons[5];
            case 6 -> patron = patrons[6];
            case 7 -> patron = patrons[7];
            case 8 -> patron = patrons[8];
            case 9 -> patron = patrons[9];
            case 10 -> patron = patrons[10];
            case 11 -> patron = patrons[11];
            default -> patron = "nieznany";
        }

        System.out.printf("Cześć %s! Rok urodzenia rzymskimi: %s. Patron: %s.%n",
                name, rzymska(year), patron);
    }

}