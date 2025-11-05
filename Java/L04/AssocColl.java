public interface AssocColl {
    
    boolean search(String key);
    double get(String key);
    void set(String key, double value);
    String[] names();

    default String defaultToString() {
        StringBuilder sb = new StringBuilder();
        String[] keys = names();
        sb.append('{');
        for (String key : keys) {
            sb.append("(").append(key).append("=").append(get(key)).append("), ");
        }
        sb.append('}');
        return sb.toString();
    }
} 
