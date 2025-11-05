public class Pair implements Cloneable{
    public final String key;
    private double value;

    public Pair(String key, double value) {
        checkKey(key);
        this.key = key;
        this.value = value;
    }

    double get() {
        return this.value;
    }

    void set(double v) {
        this.value = v;
    }

    private static void checkKey(String key) {
        if (key == null) throw new IllegalArgumentException("Key cannot be null");
        if (key.isEmpty()) throw new IllegalArgumentException("Key cannot be empty");
        if (!key.matches("^[a-z]+$")) throw new IllegalArgumentException("Key must contain only lowercase letters a-z");
    }

    @Override
    public Pair clone() {
        try {
            return (Pair) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError("Clone not supported", e);
        }
    }

    @Override
    public String toString() {
            return "(" + key + ", " + value + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Pair pair = (Pair) obj;
        return key.equals(pair.key);
    }
}
