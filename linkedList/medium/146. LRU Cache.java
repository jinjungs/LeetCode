import java.util.HashMap;
import java.util.Map;

class Node {
    int key, value;
    Node prev, next;
    Node () {};
    Node (int key) {
        this.key = key;
    };
    Node (int key, int value) {
        this.key = key;
        this.value = value;
    };
}

class DoublyLinkedList {
    Node head, tail;

    // head next 1, 2, 3, 5 prev tail
    DoublyLinkedList() {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }

    void addLast(Node node) {
        Node tailPrev = tail.prev;
        tail.prev.next = node;
        tail.prev = node;
        node.prev = tailPrev;
        node.next = tail;
    }

    void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    Node removeFirst() {
        if (head.next == tail) { return null;}

        Node lru = head.next;
        remove(lru);
        return lru;
    }

}

class LRUCache {
    private final Map<Integer, Node> cache = new HashMap<>();
    private final DoublyLinkedList dll = new DoublyLinkedList();
    private final int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) return -1;
        dll.remove(node);
        dll.addLast(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (capacity == 0) return;

        Node node = cache.get(key);

        // update value already in the map
        if (node != null) {
            node.value = value;
            dll.remove(node);
            dll.addLast(node);
            return;
        }

        // new key and exceed capacity, remove LRU
        if (cache.size() == capacity) {
            Node lru = dll.removeFirst();
            if (lru != null) cache.remove(lru.key);            
        }

        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        dll.addLast(newNode);        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */