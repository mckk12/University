public class PairProb extends Pair{
    public PairProb(String key, double value) {
        super(key, 0.0);
        set(value);
    }

    @Override
    void set(double v) {
        if (v < 0.0 || v > 1.0) {
            throw new IllegalArgumentException("Value must be between 0.0 and 1.0 inclusive");
        }
        super.set(v);
    }

    @Override
    public PairProb clone() {
        return (PairProb) super.clone();
    }
}
