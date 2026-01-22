import java.io.*;
import java.util.*;
import java.util.regex.*;

public class DataChecker {
    public static List<Integer> readNumbersFromFile(String path) throws Exception {
        List<Integer> numbers = new ArrayList<>();
        Pattern pattern = Pattern.compile("^(\\d+)?(\\s*//.*)?$");
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            for (String ln = br.readLine(); ln != null; ln = br.readLine()) {
                Matcher matcher = pattern.matcher(ln.trim());
                if (!matcher.matches()) {
                    throw new IllegalArgumentException("Invalid line format: " + ln);
                }
                String numStr = matcher.group(1);
                if (numStr != null && !numStr.isEmpty()) {
                    numbers.add(Integer.parseInt(numStr));
                }
            }
        }
        return numbers;
    }

    public static void printSortedDesc(List<Integer> numbers) {
        numbers.stream()
            .sorted(Comparator.reverseOrder())
            .forEach(System.out::println);
    }

    public static void printPrimes(List<Integer> numbers) {
        numbers.stream()
            .filter(DataChecker::isPrime)
            .forEach(System.out::println);
    }

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static void printSumLessThanN(List<Integer> numbers, int n) {
        int sum = numbers.stream()
            .filter(x -> x < n)
            .mapToInt(Integer::intValue)
            .sum();
        System.out.println(sum);
    }

    public static void printCountDivisibleByN(List<Integer> numbers, int n) {
        long count = numbers.stream()
            .filter(x -> x % n == 0)
            .count();
        System.out.println(count);
    }

    public static void main(String[] args) {
        String path = "dane.txt"; 
        int n = 1000;
        int divisor = 7; 
        try {
            List<Integer> numbers = readNumbersFromFile(path);
            System.out.println("Sorted descending:");
            printSortedDesc(numbers);
            System.out.println("Primes:");
            printPrimes(numbers);
            System.out.println("Sum < " + n + ":");
            printSumLessThanN(numbers, n);
            System.out.println("Count divisible by " + divisor + ":");
            printCountDivisibleByN(numbers, divisor);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
