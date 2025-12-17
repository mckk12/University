package structures;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class SimpleList<T extends Comparable<T>> implements SimpleSequence<T>, Iterable<T> {
    private class SimpleNode {
        private SimpleNode prev, next;
        T data;

        public SimpleNode(T data) {
            if(data == null) {
                throw new NullPointerException("Data cannot be null");
            }
            this.data = data;
        }

        void insertAfter(SimpleNode newNode) {
            newNode.prev = this;
            newNode.next = this.next;
            if(this.next != null) {
                this.next.prev = newNode;
            }
            this.next = newNode;
            modCount++;
        }

        void insertBefore(SimpleNode newNode) {
            newNode.next = this;
            newNode.prev = this.prev;
            if(this.prev != null) {
                this.prev.next = newNode;
            }
            this.prev = newNode;
            modCount++;
        }

        void remove() {
            if(this.prev != null) {
                this.prev.next = this.next;
            }
            if(this.next != null) {
                this.next.prev = this.prev;
            }
            modCount++;
        }
    }

    private SimpleNode head;

    public void insert(T el, int pos) {
        SimpleNode newNode = new SimpleNode(el);
        if(head == null) {
            head = newNode;
            return;
        }
        if(pos == 0) {
            head.insertBefore(newNode);
            head = newNode;
            return;
        }
        SimpleNode current = head;
        for(int i = 0; i < pos - 1 && current.next != null; i++) {
            current = current.next;
        }
        if (current == null) {
            throw new IndexOutOfBoundsException("Position out of bounds");
        }
        current.insertAfter(newNode);
    }

    public void remove(T el) {
        SimpleNode current = head;
        while(current != null) {
            if(current.data.equals(el)) {
                if(current == head) {
                    head = current.next;
                }
                current.remove();
                return;
            }
            current = current.next;
        }
        throw new IllegalArgumentException("Element not in list");
    }

public void removeAt(int pos) {
        if(head == null) {
            throw new IndexOutOfBoundsException("List is empty");
        }
        SimpleNode current = head;
        for(int i = 0; i < pos; i++) {
            if(current == null) {
                throw new IndexOutOfBoundsException("Position out of bounds");
            }
            current = current.next;
        }
        if(current == head) {
            head = current.next;
        }
        current.remove();
    }

    public T min() {
        if(head == null) {
            throw new IllegalStateException("List is empty");
        }
        T min = head.data;
        SimpleNode current = head.next;
        while(current != null) {
            if(current.data.compareTo(min) < 0) {
                min = current.data;
            }
            current = current.next;
        }
        return min;
    }

    public T max() {
        if(head == null) {
            throw new IllegalStateException("List is empty");
        }
        T max = head.data;
        SimpleNode current = head.next;
        while(current != null) {
            if(current.data.compareTo(max) > 0) {
                max = current.data;
            }
            current = current.next;
        }
        return max;
    }

    public boolean search(T el) {
        SimpleNode current = head;
        while(current != null) {
            if(current.data.equals(el)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public T at(int pos) {
        SimpleNode current = head;
        for(int i = 0; i < pos; i++) {
            if(current == null) {
                throw new IndexOutOfBoundsException("Position out of bounds");
            }
            current = current.next;
        }
        if(current == null) {
            throw new IndexOutOfBoundsException("Position out of bounds");
        }
        return current.data;
    }

    public int index(T el) {
        SimpleNode current = head;
        int index = 0;
        while(current != null) {
            if(current.data.equals(el)) {
                return index;
            }
            current = current.next;
            index++;
        }
        throw new IllegalArgumentException("Element not in list");
    }

    public int size() {
        SimpleNode current = head;
        int size = 0;
        while(current != null) {
            size++;
            current = current.next;
        }
        return size;
    }

    public boolean empty() {
        return head == null;
    }

    private int modCount = 0;
    private class SimpleListIterator implements Iterator<T> {
        private SimpleNode current = head;
        private int modCountOnStart;

        SimpleListIterator() {
            modCountOnStart = modCount;
        }

        private void checkValidity() {
            if(modCount != modCountOnStart) {
                throw new IllegalStateException("Iterator is no longer valid");
            }
        }

        @Override
        public boolean hasNext() {
            checkValidity();
            return current != null;
        }

        @Override
        public T next() {
            checkValidity();
            if(current == null) {
                throw new NoSuchElementException("No more elements in the list");
            }
            T data = current.data;
            current = current.next;
            return data;
        }
    }

    public Iterator<T> iterator() {
        return new SimpleListIterator();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        SimpleNode current = head;
        sb.append("[");
        while (current != null) {
            sb.append(current.data);
            current = current.next;
            if (current != null) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();   
    }
}