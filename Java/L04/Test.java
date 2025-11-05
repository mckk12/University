import java.util.Arrays;

public class Test {
    public static void main(String[] args) {
    System.out.println("---- Test Pair and PairProb ----");
    Pair p1 = new Pair("a", 1.3);
    System.out.println(p1);
    System.out.println(p1.get());
    p1.set(3.5);
    System.out.println("After set: " + p1);

    Pair p1clone = p1.clone();
    System.out.println("p1 equals p1clone by key: " + p1.equals(p1clone));


    try {
        new Pair("BadKey", 1.0);
    } catch (IllegalArgumentException e) {
        System.out.println("Caught expected invalid-key exception: " + e.getMessage());
    }

    try {
        new PairProb("p", 1.5);
    } catch (IllegalArgumentException e) {
        System.out.println("Caught expected prob-range exception: " + e.getMessage());
    }


    System.out.println("\n---- Test ArraySetVar and cloning ----");
    ArraySetVar set = new ArraySetVar(2);
    set.set("a", 1.0);
    set.set("b", 2.0);
    try {
        set.set("c", 3.0); // should fail, set is full
    } catch (IllegalStateException e) {
        System.out.println("Caught expected full-set exception: " + e.getMessage());
    }

    System.out.println("Search 'a': " + set.search("a"));
    System.out.println("Search 'c': " + set.search("c"));
    System.out.println("Get 'b': " + set.get("b"));

    System.out.println("Original set (toString):\n" + set);

    ArraySetVar setClone = set.clone();
    System.out.println("Cloned set (toString):\n" + setClone);


    // Modify clone and original to show deep cloning
    set.set("b", 20.0); // updates original
    setClone.set("a", 10.0); // updates copy


    System.out.println("After modifications:");
    System.out.println("Original:\n" + set);
    System.out.println("Clone:\n" + setClone);


    // Test deletion and names()
    set.del("b");
    System.out.println("After deleting 'b' from original:\n" + set);
    System.out.println("Names in clone: " + Arrays.toString(setClone.names()));


    // Test clear
    set.clear();
    System.out.println("After clear, original size: " + set.size() + ", content:\n" + set);
    }
}
