public interface AssociativeCollection 
extends Cloneable, AssocColl{
    void del(String key);
    int size();

    @Override
    default String defaultToString() {
        StringBuilder sb = new StringBuilder();
        String[] keys = names();
        sb.append('{');
        for (String key : keys) {
            sb.append("(").append(key).append(": ").append(get(key)).append("), ");
        }
        sb.append('}');
        return sb.toString();
    }
}