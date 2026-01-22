import java.io.*;
import java.util.*;
import java.util.regex.*;


public class DataChecker {
    public static LinkedList<Trojkat> readNumbersFromFile(String path) throws Exception {
        LinkedList<Trojkat> trojkaty = new LinkedList<>();
        Pattern pattern = Pattern.compile("^(\\d+\\p{Punct}\\d{2})?\\s*(\\d+\\p{Punct}\\d{2})?\\s*(\\d+\\p{Punct}\\d{2})?\\s*(\\s*//.*)?$");
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            for (String ln = br.readLine(); ln != null; ln = br.readLine()) {
                Matcher matcher = pattern.matcher(ln.trim());
                if (!matcher.matches()) {
                    System.out.println(matcher);
                    throw new IllegalArgumentException("Invalid line format: " + ln);
                }
                String a = matcher.group(1);
                String b = matcher.group(2);
                String c = matcher.group(3);
                if (a != null && b != null && c != null && !a.isEmpty() && !b.isEmpty() && !c.isEmpty()) {
                    try {
                        Trojkat t = new Trojkat(Double.parseDouble(a), Double.parseDouble(b), Double.parseDouble(c));
                        trojkaty.add(t);
                    } catch (IllegalArgumentException e) {
                        System.out.println("Invalid triangle sides: " + a + ", " + b + ", " + c + ". Skipping this entry.");
                        continue;
                    }
                }
            }
        }
        return trojkaty;
    }

    public static void printSortedDesc(List<Trojkat> trojkaty) {
        trojkaty.stream()
            .sorted()
            .forEach(System.out::println);
    }

    public static void printRectangularTrojkaty(List<Trojkat> trojkaty) {
        trojkaty.stream()
            .filter(t -> {
                double[] sides = {t.a, t.b, t.c};
                Arrays.sort(sides);
                return sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2];
            })
            .forEach(System.out::println);
    }

    public static void printCountEquilateralTrojkaty(List<Trojkat> trojkaty) {
        long count = trojkaty.stream()
            .filter(t -> t.a == t.b && t.b == t.c)
            .count();
        System.out.println(count);
    }

    public static void printMinMaxAreaTrojkaty(List<Trojkat> trojkaty) {
        Optional<Trojkat> minAreaTrojkat = trojkaty.stream()
            .min((t1, t2) -> {
                double s1 = (t1.a + t1.b + t1.c) / 2;
                double area1 = Math.sqrt(s1 * (s1 - t1.a) * (s1 - t1.b) * (s1 - t1.c));
                double s2 = (t2.a + t2.b + t2.c) / 2;
                double area2 = Math.sqrt(s2 * (s2 - t2.a) * (s2 - t2.b) * (s2 - t2.c));
                return Double.compare(area1, area2);
            });
        Optional<Trojkat> maxAreaTrojkat = trojkaty.stream()
            .max((t1, t2) -> {
                double s1 = (t1.a + t1.b + t1.c) / 2;
                double area1 = Math.sqrt(s1 * (s1 - t1.a) * (s1 - t1.b) * (s1 - t1.c));
                double s2 = (t2.a + t2.b + t2.c) / 2;
                double area2 = Math.sqrt(s2 * (s2 - t2.a) * (s2 - t2.b) * (s2 - t2.c));
                return Double.compare(area1, area2);
            });

        minAreaTrojkat.ifPresent(t -> System.out.println("Triangle with minimum area: " + t));
        maxAreaTrojkat.ifPresent(t -> System.out.println("Triangle with maximum area: " + t));
    }


    

    public static void main(String[] args) {
        String path = "trojkaty.txt"; 
        try {
            LinkedList<Trojkat> trojkaty = readNumbersFromFile(path);
            System.out.println("Trojkaty posortowane rosnaco wedlug obwodu:");
            printSortedDesc(trojkaty);

            System.out.println("\nTrojkaty prostokatne:");
            printRectangularTrojkaty(trojkaty);

            System.out.println("\nTrojkaty rownoboczne:");
            printCountEquilateralTrojkaty(trojkaty);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
