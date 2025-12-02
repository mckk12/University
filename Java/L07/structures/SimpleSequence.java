package structures;

public interface SimpleSequence<T extends Comparable<T>> {
    void insert(T el, int pos);
    void remove(T el);
    void removeAt(int pos);
    T min();
    T max();
    boolean search(T el);
    T at(int pos);
    int index(T el);
    int size();
    boolean empty();
}

