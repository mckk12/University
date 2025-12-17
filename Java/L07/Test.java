import structures.SimpleList;

import java.util.Date;

public class Test {
    public static void main(String[] args) {
        System.out.println("--- Testing SimpleList<Integer> ---");
        SimpleList<Integer> li = new SimpleList<>();
        li.insert(3, 0);
        li.insert(1, 0);
        li.insert(2, 2); // [1,3,2]
        System.out.println(li + " size=" + li.size() + " empty=" + li.empty());
        System.out.println("min=" + li.min() + " max=" + li.max());
        System.out.println("search 3: " + li.search(3) + " index of 3: " + li.index(3));
        System.out.println("element at index 0: " + li.at(0));
        li.remove(1); // remove element 1
        System.out.println(li);
        li.removeAt(0);
        System.out.println(li);
        li.removeAt(0);
        System.out.println(li + " size=" + li.size() + " empty=" + li.empty());
        li.insert(10, 0);
        li.insert(20, 1);
        li.insert(15, 1);
        System.out.println("iterate:");
        for (Integer x : li) System.out.println(x);


        System.out.println("--- Testing SimpleList<String> ---");
        SimpleList<String> ls = new SimpleList<>();
        ls.insert("b", 0);
        ls.insert("a", 0);
        ls.insert("c", 2);
        System.out.println(ls + " size=" + ls.size() + " empty=" + ls.empty());
        System.out.println("min=" + ls.min() + " max=" + ls.max());
        System.out.println("search 'b': " + ls.search("b") + " index of 'b': " + ls.index("b"));
        System.out.println("element at index 0: " + ls.at(0));
        ls.remove("a");
        System.out.println(ls);
        ls.removeAt(0);
        System.out.println(ls);
        ls.removeAt(0);
        System.out.println(ls + " size=" + ls.size() + " empty=" + ls.empty());
        ls.insert("x", 0);
        ls.insert("y", 1);
        ls.insert("z", 1);
        System.out.println("iterate:");
        for (String s : ls) System.out.println(s);        


        System.out.println("--- Testing SimpleList<Date> ---");
        SimpleList<Date> ld = new SimpleList<>();
        ld.insert(new Date(1000000000L), 0);
        ld.insert(new Date(0L), 1);
        ld.insert(new Date(500000000L), 1);
        System.out.println(ld + " size=" + ld.size() + " empty=" + ld.empty());
        System.out.println("min=" + ld.min() + " max=" + ld.max());
        System.out.println("search Date(500000000L): " + ld.search(new Date(500000000L)) + " index: " + ld.index(new Date(500000000L)));
        System.out.println("element at index 0: " + ld.at(0));
        ld.remove(new Date(0L));
        System.out.println(ld);
        ld.removeAt(0);
        System.out.println(ld);
        ld.removeAt(0);
        System.out.println(ld + " size=" + ld.size() + " empty=" + ld.empty());
        ld.insert(new Date(2000000000L), 0);
        ld.insert(new Date(1500000000L), 1);
        ld.insert(new Date(1750000000L), 1);
        System.out.println("iterate:");
        for (Date d : ld) System.out.println(d);


        try {
            System.out.println("Testing iterator invalidation:");
            for (Integer x : li) {
            System.out.println(x);
            li.insert(99, li.size()); 
        }
        } catch (Exception ex) {
            System.out.println("Expected exception: " + ex);
        }
        }

}
