public class ArraySetVar extends SetVar{
    protected Pair[] vars;
    protected int siz;

    public ArraySetVar(int capacity){
        if(capacity <= 0) throw new IllegalArgumentException("Capacity must be positive");
        this.vars = new Pair[capacity];
        this.siz = 0;
    }

    public ArraySetVar clone(){
        ArraySetVar cloned = new ArraySetVar(this.vars.length);
        for(int i = 0; i < this.siz; i++){
            cloned.vars[i] = this.vars[i].clone();
        }
        cloned.siz = this.siz;
        return cloned;
    }

    public void clear(){
        for(int i = 0; i < this.siz; i++){
            this.vars[i] = null;
        }
        this.siz = 0;
    }

    public void del(String key){
        for(int i = 0; i < this.siz; i++){
            if(this.vars[i].key.equals(key)){
                this.vars[i] = this.vars[this.siz - 1];
                this.vars[this.siz - 1] = null;
                this.siz--;
                return;
            }
        }
        throw new IllegalArgumentException("Key not found: " + key);
    }

    public int size(){
        return this.siz;
    }

    public double get(String key){
        for(int i = 0; i < this.siz; i++){
            if(this.vars[i].key.equals(key)){
                return this.vars[i].get();
            }
        }
        throw new IllegalArgumentException("Key not found: " + key);
    }

    public void set(String key, double value){
        for(int i = 0; i < this.siz; i++){
            if(this.vars[i].key.equals(key)){
                this.vars[i].set(value);
                return;
            }
        }
        if(this.siz >= this.vars.length){
            throw new IllegalStateException("SetVar is full");
        }
        this.vars[this.siz++] = new Pair(key, value);
    }

    public String[] names(){
        String[] names = new String[this.siz];
        for(int i = 0; i < this.siz; i++){
            names[i] = this.vars[i].key;
        }
        return names;
    }

    public boolean search(String key){
        for(int i = 0; i < this.siz; i++){
            if(this.vars[i].key.equals(key)){
                return true;
            }
        }
        return false;
    }
    
    @Override
    public String toString(){
        return defaultToString();
    }
}
